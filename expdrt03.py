import time
from rtPeak03 import rtPeak

arry = [
  2818,2821,2817,2823,2821,2817,2816,2818,2819,2817,
  2815,2818,2835,2838,2870,2841,2827,2798,2869,2832,
  2817,2830,2815,2838,2824,2817,2819,2821,2818,2817,
  2825,2820,2815,2819,2816,2821,2816,2817,2820,2820,
  2816,2833,2882,2817,2820,2831,2857,2832,2839,2817,
  2820,2815,2865,2815,2816,2790,2819,2818,2817,2819,
  2816,2819,2817,2818,2829,2835,2864,2831,2823,2822,
  2859,2837,2822,2829,2828,2896,2850,2823,2817,2817,
  2799,2821,2816,2816,2821,2815,2816,2816,2816,2815,
  2815,2829,2870,2859,2823,2802,2817,2837,2830,2843,
  2822,2821,2824,2849,2842,2822,2818,2817,2815,2817,
  2811,2815,2815,2813,2816,2816,2819,2815,2816,2813,
  2816,2809,2830,2818,2832,2818,2893,2812,2821,2817,
  2847,2812,2815,2815,2815,2818,2817,2816,2815,2817,
  2814,2819,2811,2815,2819,2818,2816,
  #-------------------------------------------------
  # 2799,2799,2800,2799,2802,2800,2798,2800,2800,2802,
  # 2800,2794,2800,2799,2800,2799,2841,3002,3155,2810,
  # 2823,2992,2922,2798,2795,2817,2799,2814,2800,2802,
  # 2801,2800,2801,2768,2810,2883,2878,2867,2809,2867,
  # 2811,2863,2961,2902,2819,2814,2822,3246,2864,2816,
  # 2813,2813,2816,2805,2767,2807,2794,2801,2819,2805,
  # 2800,2807,2864,3099,3158,2834,2845,3259,3191,2817,
  # 2805,2801,2810,2807,2821,2725,2820,2815,2849,3135,
  # 3638,2887,2815,2813,2866,2992,3218,2847,2815,2817,
  # 2885,3254,3280,2831,2799,2795,2797,2797,2795,2797,
  # 2795,2800,2800,2800,2800,2807,2905,3413,3323,2858,
  # 3003,3421,2858,2807,2804,2801,2805,2808,2805,2829,
  # 3151,3540,2878,2817,2854,3295,4095,2991,2822,2814,
  # 2989,4095,3315,2811,2800,2861,2800,2797,2813,2781,
  # 2796,2800,2798,2798,2797,2800,2798,
  # #-------------------------------------------------
  # 2800,2800,2813,2799,2800,2797,2746,2800,2798,2809,
  # 2794,2783,2781,2702,2494,2399,2480,2670,2736,2635,
  # 2557,2557,2625,2753,2768,2778,2773,2781,2774,2770,
  # 2768,2777,2775,2751,2645,2474,2383,2477,2693,2701,
  # 2622,2608,2667,2765,2683,2559,2559,2669,2751,2778,
  # 2778,2791,2790,2790,2815,2787,2787,2783,2764,2651,
  # 2599,2630,2704,2626,2464,2457,2711,2770,2881,2784,
  # 2782,2788,2784,2683,2319,2319,2589,2699,2750,2685,
  # 2595,2527,2608,2715,2733,2601,2455,2524,2730,2772,
  # 2786,2791,2795,2794,2795,2797,2795,2797,2795,2800,
  # 2797,2816,2791,2800,2799,2800,2795,2803,2800,2800,
  # 2797,2784,2800,2802,2807,2800,2799,2800,2795,2795,
  # 2795,2800,2807,2800,2800,2793,2799,2800,
]

tms=100

# lny = 9 #num impar
# dt=4 # dt < t VALIDAR!!!
# base=3000
# threshold = 300
# p1 = rtPeak(lny, dt, base, threshold)

pkp1 = rtPeak(3, 1, 2800, 50)

num = 0
while num < len(arry):
  #-----------------------------------------------------
  pk = pkp1.runPD(arry[num])
  print(pk)
  #-----------------------------------------------------
  time.sleep(tms/1000)
  num += 1