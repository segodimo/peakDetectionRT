import time
from rtPeak09 import rtPeak

arry = [
  # 2834,2832,2832,2819,2835,2833,2827,2835,2833,2829,
  # 2832,2847,2819,2831,2832,2834,2832,2845,2832,2800,
  # 2832,2837,2832,2826,2832,2830,2831,2825,2823,2832,
  # 2830,2831,2826,2833,2830,2827,2854,2833,2829,2831,
  # 2829,2826,2830,2833,2832,2806,2831,2832,2831,2830,
  # 2831,2838,2830,2827,2829,2831,2832,2830,2831,2832,
  # 2831,2831,2829,2832,2832,2832,2831,2853,2832,2832,
  # 2823,2829,2825,2827,2828,2828,2829,2832,2832,2832,
  # 2832,2827,2832,2827,2832,2851,2962,2887,2834,2819,
  # 2833,2835,2838,2834,2827,2834,2842,2839,2839,2848,
  # 2955,3012,2837,2835,2863,2832,2827,2832,2832,2832,
  # 2832,2832,2832,2832,2830,2832,2832,2832,2829,2847,
  # 2834,
  2905,3658,3199,2837,2831,2854,2833,2831,2843,
  2844,2835,2835,2842,2833,2833,2839,2832,2837,2832,
  2842,2833,2804,2852,2971,4095,4095,3049,2843,2847,
  2837,2857,2839,2846,2917,3824,4095,4095,2915,2830,
  2825,2815,2819,2826,2827,2817,2825,2816,2822,2829,
  2819,2824,2821,2803,2813,2779,2608,2497,2547,2537,
  2578,2752,2800,2806,2818,2826,2783,2557,2463,2598,
  2365,2642,2800,2816,2815,2819,2816,2818,2821,2827,
  2815,2815,2816,2834,2818,2821,2822,2819,2823,2845,
  2826,2822,2819,2835,2827,2825,2810,2831,2829,2831,
  2831,2832,2829,2829,2827,2829,2822,2823,2830,2901,
  3153,2921,2822,2830,2825,2831,2834,2945,2997,2834,
  2834,2825,2836,2829,2823,2827,2819,2831,2829,2830,
  2827,2822,2825,2831,2821,2827,2827,2829,2931,4095,
  4095,3209,2843,2826,2832,2830,2832,2853,3683,4095,
  4095,2855,2822,2826,2800,2825,2829,2829,2828,2833,
  2832,2827,2827,2827,2829,2831,2975,4095,4095,2882,
  2832,2827,2825,2822,2821,2820,2820,2820,2826,2818,
  2842,2822,2805,2819,2821,2825,2818,2817,2815,2821,
  2821,2784,2679,2649,2667,2683,2741,2791,2887,2807,
  2805,2801,2715,2614,2624,2576,2743,2813,2815,2818,
  2815,2843,2816,2827,2816,2820,2819,2819,2818,2819,
  2815,2813,2817,2819,2810,2782,2821,2819,2790,2818,
  2809,2821,2816,2822,2825,2819,2818,2820,2819,2820,
  2819,2818,2811,2821,2823,2823,
]
tms=100

pkp1 = rtPeak(3,1,[2600, 2900, 3450],['m','j','u'])

num = 0
while num < len(arry):
  #-----------------------------------------------------
  pk = pkp1.runPdRt(arry[num])
  if pk[0]: print(pk)
  #-----------------------------------------------------
  time.sleep(tms/1000)
  num += 1