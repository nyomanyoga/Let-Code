class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        import sys

        n = len(stones)
        kMax = sys.maxsize  # Nilai maksimum sebagai pengganti infinity

        # Jika jumlah tumpukan tidak memungkinkan penggabungan menjadi satu pile
        if (n - 1) % (k - 1) != 0:
            return -1

        # Implementasi manual prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # DP array: dp[i][j][p] menyimpan biaya minimum untuk menggabungkan
        # stones[i:j+1] menjadi p piles
        dp = [[[kMax] * (k + 1) for _ in range(n)] for _ in range(n)]

        # Inisialisasi: biaya 0 untuk 1 pile jika hanya ada satu elemen
        for i in range(n):
            dp[i][i][1] = 0

        # Iterasi panjang interval
        for length in range(2, n + 1):  # Panjang interval
            for i in range(n - length + 1):
                j = i + length - 1  # Akhir interval
                for piles in range(2, k + 1):  # Jumlah tumpukan
                    for mid in range(i, j, k - 1):  # Pembagian interval
                        dp[i][j][piles] = min(dp[i][j][piles],
                                              dp[i][mid][1] + dp[mid + 1][j][piles - 1])
                # Jika ingin menggabungkan menjadi satu pile
                if dp[i][j][k] < kMax:
                    dp[i][j][1] = dp[i][j][k] + prefix[j + 1] - prefix[i]

        # Hasil akhir adalah biaya minimum untuk menggabungkan seluruh interval menjadi satu pile
        return dp[0][n - 1][1] if dp[0][n - 1][1] < kMax else -1
