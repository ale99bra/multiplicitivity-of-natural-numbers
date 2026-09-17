import numpy as np
import matplotlib.pyplot as plt
import os

def create_labels(mult):
    pentanome = 1*2*3*5*7

    tot_mono = len([n for n in mult if n== 1])
    tot_duo = len([n for n in mult if n== 2])
    tot_tri = len([n for n in mult if n== 3])
    tot_quad = len([n for n in mult if n== 4])
    tot_penta = len([n for n in mult if n== 5])


    count1 =  len([n for n in mult[:pentanome] if n== 1])
    count2 = len([n for n in mult[:pentanome] if n== 2])
    count3 = len([n for n in mult[:pentanome] if n== 3])
    count4 = len([n for n in mult[:pentanome] if n== 4])
    count5 = len([n for n in mult[:pentanome] if n== 5])

    count12 =  len([n for n in mult[pentanome:pentanome*2] if n== 1])
    count22 = len([n for n in mult[pentanome:pentanome*2] if n== 2])
    count32 = len([n for n in mult[pentanome:pentanome*2] if n== 3])
    count42 = len([n for n in mult[pentanome:pentanome*2] if n== 4])
    count52 = len([n for n in mult[pentanome:pentanome*2] if n== 5])

    count13 =  len([n for n in mult[pentanome*2:pentanome*3] if n== 1])
    count23 = len([n for n in mult[pentanome*2:pentanome*3] if n== 2])
    count33 = len([n for n in mult[pentanome*2:pentanome*3] if n== 3])
    count43 = len([n for n in mult[pentanome*2:pentanome*3] if n== 4])
    count53 = len([n for n in mult[pentanome*2:pentanome*3] if n== 5])

    count14 =  len([n for n in mult[pentanome*3:pentanome*4] if n== 1])
    count24 = len([n for n in mult[pentanome*3:pentanome*4] if n== 2])
    count34 = len([n for n in mult[pentanome*3:pentanome*4] if n== 3])
    count44 = len([n for n in mult[pentanome*3:pentanome*4] if n== 4])
    count54 = len([n for n in mult[pentanome*3:pentanome*4] if n== 5])

    labels = ["monome", "duome", "triome", "quadrome", "pentanome"]
    range_tot = [tot_mono, tot_duo, tot_tri, tot_quad, tot_penta]
    range1 = [count1, count2, count3, count4, count5]
    range2 = [count12, count22, count32, count42, count52]
    range3 = [count13, count23, count33, count43, count53]
    range4 = [count14, count24, count34, count44, count54]

    return labels, [range_tot, range1, range2, range3, range4]

# Define array
N = 100000
nums = np.linspace(1, N, N).astype(int)

# Create list for multiplicitivity
mult = []
for num in nums:
    if num == 1: 
        mult.append(0)
        continue
    i = 1
    if num % 2 == 0 and num != 2:
        i += 1
    if num % 3 == 0 and num != 3:
        i += 1
    if num % 5 == 0 and num != 5:
        i += 1
    if num % 7 == 0 and num != 7:
        i += 1

    mult.append(i)

# Create labels and classes for histograms
labels, ranges = create_labels(mult)
x = np.arange(len(labels))
pentanome = 1*2*3*5*7

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")
os.makedirs("paper", exist_ok=True)
fig_path = os.path.join("paper","figures")
os.makedirs(fig_path, exist_ok=True)

# Histograms
## total
plt.figure()
plt.bar(x, ranges[0], width=0.8, color = "black")
plt.xticks(x, labels)
plt.title(f"Distribution of the first {len(nums)} natural numbers")
plt.savefig(os.path.join(fig_path, "dist_tot.png"))

## First 210 nums
plt.figure()
plt.bar(x, ranges[1], width=0.8)
plt.xticks(x, labels)
plt.title("Distribution of the numbers from 1 to 210")
plt.savefig(os.path.join(fig_path, "dist_1_210.png"))
## Different ranges
width = 0.2
plt.figure()
plt.bar(x - 1.5*width, ranges[1], width, label=f'[1,{pentanome}]')
plt.bar(x - 0.5*width, ranges[2], width, label=f'[{pentanome+1},{pentanome*2}]')
plt.bar(x + 0.5*width, ranges[3], width, label=f'[{pentanome*2+1},{pentanome*3}]')
plt.bar(x + 1.5*width, ranges[4], width, label=f'[{pentanome*3+1},{pentanome*4}]')
plt.xticks(x, labels)
plt.legend()
plt.title("Distribution of the numbers in ranges")
plt.savefig(os.path.join(fig_path, "dist_ranges.png"))

# Display pattern for the first 2000 numbers
display_num = 2000
plt.figure(figsize=(16,8))
plt.scatter(nums, mult, marker=".")
plt.xlim(1, display_num)
plt.ylabel("Multiplicitivity")
plt.title(f"Multiplicitivity of the first {display_num} numbers")
plt.savefig(os.path.join(fig_path, "pattern.png"))

# Display patter of multiple ranges
plt.figure(figsize=(16,8))
plt.scatter(nums[:pentanome], mult[:pentanome], marker="o", color="blue", label = f"[1, {pentanome}]")
plt.scatter(nums[:pentanome], mult[pentanome:pentanome*2], marker="x", color="orange", label = f"[{pentanome+1}, {pentanome*2}]")
plt.scatter(nums[:pentanome], mult[pentanome*2:pentanome*3], marker="_", color="green", label = f"[{pentanome*2+1}, {pentanome*3}]")
plt.scatter(nums[:pentanome], mult[pentanome*3:pentanome*4], marker="*", color="red", label = f"[{pentanome*3+1}, {pentanome*4}]")
plt.vlines(210, 0, 5, linestyles="--", color = "grey", label="210th number")
plt.vlines(105, 0, 5, linestyles="--", color = "brown", label="105th number")
plt.legend()
plt.ylabel("Multiplicitivity")
plt.xlabel("Number since beginning of range")
plt.title("Discovered pattern of numbers")
plt.savefig(os.path.join(fig_path, "pattern_ranges.png"))