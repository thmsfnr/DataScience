
library(shiny)
library(shinythemes)

# Define UI for the application
shinyUI(fluidPage(

  includeCSS("./style.css"),
  theme = shinytheme("superhero"),

  # Application header
  titlePanel(h2(align="center","Energie en France")),
  fluidRow(h4(align="center","Ce projet est une analyse de la sortie du nucléaire dans la production d'électricité française réalisée lors d'un cours à Polytech Montpellier.")),
  fluidRow(h3("")),

  sidebarLayout(

    # Sidebar
    sidebarPanel(

      # More information about the project
      p("Ce projet visait initialement à nous permettre d'approfondir certaines connaissances acquises au cours de notre formation, d'en découvrir d'autres, d'identifier des méthodes appropriées pour répondre à un objectif donné, de combiner des méthodes complémentaires, de comparer des méthodes concurrentes pour répondre à des objectifs donnés, d'interpréter et éventuellement de comparer les résultats des méthodes mises en œuvre, ainsi que d'avoir un esprit critique vis-à-vis de la collecte des données, des méthodes mises en œuvre et de leur paramétrage."),
      p("Concernant le sujet, nous avions le choix entre différents thèmes et nous avons choisi celui lié à l'étude des données ouvertes, plus précisément lié au projet d'Université des données ouvertes mené par l'association Latitudes en lien avec le site institutionnel national data gouv. Les jeux de données de ce thème sont alors multiples, sachant que nous avons fait le choix d'étudier celui associé à l'énergie en France."),
      p("Concernant la problématique, nous en avons choisi une qui diffère de celle proposée dans le projet. Au lieu de centrer notre étude sur les conséquences énergétiques de la guerre en Ukraine, nous avons déterminer les conséquences de la fin du nucléaire dans la production d'électricité en France."),
      a(href = "https://github.com/thmsfnr/DataScience", "Cliquez ici pour plus d'informations"),
      tags$hr(style = "border:0.8px solid white;"),

      # If "Conséquences sur le prix et l'environnement" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Conséquences sur prix et environnement'",
        h4(align="center","Choix de la répartition des différentes filières de production"),
        sliderInput("hydraulic","Hydraulique:",min = 0, max = 100,value = c(9)),
        sliderInput("nuclear","Nucléaire:",min = 0, max = 100,value = c(76)),
        sliderInput("wind","Eolien:",min = 0, max = 100,value = c(2)),
        sliderInput("solar","Photovolatique:",min = 0, max = 100,value = c(2)),
        sliderInput("gas","Gaz:",min = 0, max = 100,value = c(7)),
        sliderInput("coal","Charbon:",min = 0, max = 100,value = c(2)),
        sliderInput("oil","Fioul:",min = 0, max = 100,value = c(2)),
      ),

      # If "Production" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Production'",

      ),

      # If "Consommation" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Consommation'",

      ),

      # If "Lien entre production et consommation" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Lien entre production et consommation'",

      ),

      # If "Confrontation des prédictions" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Confrontation des prédictions'",

      )
    ),

    # Main
    mainPanel(
      navbarPage("Menu",id = "tabSelected",

        # Display of graphics according to the selected menu
        navbarMenu("Fenetres",
          tabPanel("Conséquences sur prix et environnement",
            h3(style = "text-align:center; margin-bottom: 40px; margin-top: 20px;","Conséquences sur le prix et l'environnement"),
            tags$h1(class = "alert alert-dismissible alert-warning price",
            textOutput("prix")),
            tags$h1(class = "alert alert-dismissible alert-warning price",
                textOutput("environnement")
            )
          ),
          tabPanel("Production",),
          tabPanel("Comsommation",),
          tabPanel("Lien entre production et consommation",),
          tabPanel("Confrontation des prédictions",
            h3(style = "text-align:center","Confrontation des prédictions"),
            h4(style = "margin-bottom: 40px; margin-top: 40px; margin-right: 40px; margin-left: 40px;","Les résultats de notre étude, qui se termine en 2030, nous permettent d'identifier le scénario vers lequel nous nous dirigeons vis-à-vis du  ", tags$a("rapport de RTE", href = "https://assets.rte-france.com/prod/public/2021-12/Futurs-Energetiques-2050-principaux-resultats.pdf"), " de 2021 relatif au futur énergétique en 2050. Ainsi, nos prédictions indiquent que nous allons vers le scénario N03 dans lequel le mix de production repose à parts égales sur les énergies renouvelables et sur le nucléaire à l’horizon 2050. Pour plus de détails, voici ci-dessous la liste de tous les scénarios illustrés dans ce rapport de RTE:"),
            tags$div(style = "text-align: center;",
              imageOutput("mix")
            )
          )
        )
      )
    )

  )
))
