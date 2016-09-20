if(dynamic_cast<Fireball*>(spell))
    dynamic_cast<Fireball*>(spell)->revealFirepower();
else if(dynamic_cast<Frostbite*>(spell))
    dynamic_cast<Frostbite*>(spell)->revealFrostpower();
else if(dynamic_cast<Thunderstorm*>(spell))
    dynamic_cast<Thunderstorm*>(spell)->revealThunderpower();
else if(dynamic_cast<Waterbolt*>(spell))
    dynamic_cast<Waterbolt*>(spell)->revealWaterpower();
else {
    /* This block of code is originally from geeksforgeeks.org, but modified for
     * our purposes. I will write one from scatch sometime in the future. */
    /* Beginning of LCS algorithm */
    string X = spell->revealScrollName();
    string Y = SpellJournal::read();
    int m = X.length();
    int n = Y.length();

    int L[m+1][n+1];
    int i, j;

    for (i=0; i<=m; i++)
    {
        for (j=0; j<=n; j++)
        {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else
                if (X[i-1] == Y[j-1])
                        L[i][j] = L[i-1][j-1] + 1;
                else
                    L[i][j] = std::max(L[i-1][j], L[i][j-1]);
        }
    }
    /* End of LCS algorithm */
    std::cout << std::to_string(L[m][n]) << std::endl;
}
