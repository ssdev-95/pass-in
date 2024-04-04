CREATE TABLE "tb_events" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "details" TEXT,
    "slug" TEXT NOT NULL,
    "maximum_attendees" INTEGER,
		"start_date" DATETIME NOT NULL,
		"end_date" DATETIME NOT NULL,
		CONSTRAINT "events_cannot_lie_in_the_past" CHECK ("start_date" > CURRENT_TIMESTAMP)
		CONSTRAINT "events_cannot_lie_in_the_past" CHECK ("end_date" > "start_date")
);

CREATE TABLE "tb_attendees" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "event_id" TEXT NOT NULL,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "attendees_event_id_fkey" FOREIGN KEY ("event_id") REFERENCES "tb_events" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "tb_check_ins" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "attendee_id" TEXT NOT NULL,
    CONSTRAINT "check_ins_attendeeId_fkey" FOREIGN KEY ("attendee_id") REFERENCES "tb_attendees" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE UNIQUE INDEX "events_slug_key" ON "tb_events"("slug");
CREATE UNIQUE INDEX "attendees_event_id_email_key" ON "tb_attendees"("event_id", "email");
CREATE UNIQUE INDEX "check_ins_attendeeId_key" ON "tb_check_ins"("attendee_id");
