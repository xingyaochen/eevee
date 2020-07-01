# Load package
devtools::install_github("mattflor/chorddiag")
library(chorddiag)
library(htmlwidgets)

# Create data
m <- matrix(c(5, 0, 0, 1, 1, 0, 0, 0, 3,
              0, 5, 1, 0, 1, 1, 3, 1, 0,
              0, 1, 4, 1, 1, 2, 2, 2, 0,
              0, 0, 1, 5, 0, 1, 1, 1, 1,
              1, 1, 1, 0, 5, 1, 1, 1, 1,
              0, 1, 2, 1, 1, 4, 2, 1, 0,
              0, 3, 2, 1, 1, 2, 5, 2, 0,
              0, 1, 2, 1, 1, 1, 2, 5, 0,
              3, 0, 0, 1, 1, 0, 0, 0, 4),
            byrow = TRUE,
            nrow = 9, ncol = 9)

# A vector of 9 colors for 9 groups
eevees <- c('eevee', 'vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'glaceon', 'leafeon', 'sylveon')
dimnames(m) <- list(have = eevees,
                    prefer = eevees)
groupColors <- c('#C59161', '#7CCEE6', '#F8CE6A', '#EA824F', '#DCBFD5', '#4B5A5D', 
                 '#B7E1DD', '#9DD3AF', '#F790AB')

# Build the chord diagram:
p <- chorddiag(m, groupColors = groupColors, groupnamePadding = 10, showTicks = F)
p

saveWidget(p, file=paste0( getwd(), "/eevee_chord_interactive.html"))
