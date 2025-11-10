#import "@local/report-template-typst:0.1.0": conf, azuluc3m

#show: conf.with(
  degree: "DB in Telecomunication Technologies and Data Science",
  subject: "Programming",
  year: (24, 25),
  project: "Final Project",
  title: "Mario Bros.",
  group: 196,
  bibliography-content: bibliography("bib.bib"),
  appendixes: include "apendixes.typ",
  authors: (
    (
      name: "Samuel",
      surname: "Matamoros Alonso",
      nia: 100583032
    ),
    (
      name: "Darío",
      surname: "Castro Vila",
      nia: 100581710
    ),
  ),
  // team: "Los chungitos",
  professor: "Ángel García Olaya",
  toc: true,
  logo: "new",
  language: "en"
)

#set table(
      stroke: none,
      fill: (x, y) => if calc.even(y) == false { azuluc3m.transparentize(80%) },
      inset: (x: 1.0em, y: 0.5em),
      gutter: 0.2em, row-gutter: 0em, column-gutter: 0em
    )
#show table.cell.where(y: 0) : set text(weight: "bold")

= Introduction
