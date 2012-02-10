test.score.quadratic.weighted.kappa <- function()
{
    rater.a = c(1, 2, 1)
    rater.b = c(1, 2, 2)
    kappa = ScoreQuadraticWeightedKappa(rater.a, rater.b)
    checkEqualsNumeric(kappa, 0.4)

    rater.a = c(1, 2, 3, 1, 2, 3)
    rater.b = c(1, 2, 3, 1, 3, 2)
    kappa = ScoreQuadraticWeightedKappa(rater.a, rater.b)
    checkEqualsNumeric(kappa, 0.75)

    rater.a = c(1, 2, 3)
    rater.b = c(1, 2, 3)
    kappa = ScoreQuadraticWeightedKappa(rater.a, rater.b)
    checkEqualsNumeric(kappa, 1.0)
}

test.mean.quadratic.weighted.kappa <- function()
{
    kappa = MeanQuadraticWeightedKappa( c(1, 1) )
    checkEqualsNumeric(kappa, 0.999)

    kappa = MeanQuadraticWeightedKappa( c(1, -1) )
    checkEqualsNumeric(kappa, 0.0)

    kappa = MeanQuadraticWeightedKappa( c(.5, .8), c(1.0, .5) )
    checkEqualsNumeric(kappa, 0.624536446425734)
}   
