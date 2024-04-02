CREATE TABLE "eventos" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "titulo" TEXT NOT NULL,
    "detalhes" TEXT,
    "slug" TEXT NOT NULL,
    "maximoParticipantes" INTEGER
);

CREATE TABLE "participantes" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "nome" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "evento_id" TEXT NOT NULL,
    "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "participantes_evento_id_fkey" FOREIGN KEY ("evento_id") REFERENCES "eventos" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "check_ins" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "dataCriacao" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "participanteId" TEXT NOT NULL,
    CONSTRAINT "check_ins_participanteId_fkey" FOREIGN KEY ("participanteId") REFERENCES "participantes" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE UNIQUE INDEX "eventos_slug_key" ON "eventos"("slug");
CREATE UNIQUE INDEX "participantes_event_id_email_key" ON "participantes"("event_id", "email");
CREATE UNIQUE INDEX "check_ins_participanteId_key" ON "check_ins"("participanteId");
