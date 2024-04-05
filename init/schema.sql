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
    "eventoId" TEXT NOT NULL,
    "dataCriacao" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "participantes_eventoId_fkey" FOREIGN KEY ("eventoId") REFERENCES "eventos" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "checkIns" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "dataCriacao" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "participanteId" TEXT NOT NULL,
    CONSTRAINT "checkIns_participanteId_fkey" FOREIGN KEY ("participanteId") REFERENCES "participantes" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE UNIQUE INDEX "eventos_slug_key" ON "eventos"("slug");
CREATE UNIQUE INDEX "participantes_eventoId_email_key" ON "participantes"("eventoId", "email");
CREATE UNIQUE INDEX "checkIns_participanteId_key" ON "checkIns"("participanteId");
