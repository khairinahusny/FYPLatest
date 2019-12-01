"""

======================================================================================
                        Calculating Visual Working Memory
======================================================================================

Input variables
---------------
* ``score`` : Accuracy Score of player
* ``duration`` : Time taken for the player each level

Output variable
---------------
* ``visual`` : Visual Working Memory

"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


def calcVisual(visual_score_in, visual_duration_in, show_visual_graph):
    # Generate universe variables
    v_score = visual_score_in
    v_duration = visual_duration_in
    visualScore = np.arange(0, 100, 1)
    visualDuration = np.arange(0, 61, 1)
    visual = np.arange(0, 21, 1)

    # Generate fuzzy membership functions
    avg_score_lo = fuzz.trapmf(visualScore, [0, 0, 20, 40])
    avg_score_md = fuzz.trapmf(visualScore, [20, 40, 60, 80])
    avg_score_hi = fuzz.trapmf(visualScore, [60, 80, 100, 120])

    avg_duration_lo = fuzz.trapmf(visualDuration, [0, 0, 10, 20])
    avg_duration_md = fuzz.trapmf(visualDuration, [10, 20, 30, 40])
    avg_duration_hi = fuzz.trapmf(visualDuration, [30, 40, 50, 60])

    visual_lo = fuzz.trapmf(visual, [0, 0, 5, 8])
    visual_md = fuzz.trapmf(visual, [5, 8, 13, 16])
    visual_hi = fuzz.trapmf(visual, [13, 16, 20, 20])

    # Visualizing membership functions
    fig1, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(visualScore, avg_score_lo, 'b', linewidth=1.5, label='Poor')
    ax0.plot(visualScore, avg_score_md, 'g', linewidth=1.5, label='Average')
    ax0.plot(visualScore, avg_score_hi, 'r', linewidth=1.5, label='Great')
    ax0.set_title('Accuracy Score')
    ax0.legend()

    # plotting graph for duration at Level 1:
    ax1.plot(visualDuration, avg_duration_lo, 'b', linewidth=1.5, label='Fast')
    ax1.plot(visualDuration, avg_duration_md, 'g', linewidth=1.5, label='Medium')
    ax1.plot(visualDuration, avg_duration_hi, 'r', linewidth=1.5, label='Slow')
    ax1.set_title('Duration ')
    ax1.legend()

    # plotting graph for visual WM:
    ax2.plot(visual, visual_lo, 'b', linewidth=1.5, label='Low')
    ax2.plot(visual, visual_md, 'g', linewidth=1.5, label='Medium')
    ax2.plot(visual, visual_hi, 'r', linewidth=1.5, label='High')
    ax2.set_title('Visual Working Memory')
    ax2.legend()

    # Turn off top/right axes
    for ax in (ax0, ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_visual_graph:
        plt.tight_layout()

    """
    Fuzzy rules
    -----------

    1. IF duration is low AND Score is low, THEN Visual is Medium
    2. IF duration is low AND Score is medium, THEN Visual is Medium
    3. IF duration is low AND Score is high, THEN Visual is High
    4. IF duration is medium AND Score is low, THEN Visual is Medium
    5. IF duration is medium AND Score is medium, THEN Visual is Medium
    6. IF duration is medium AND Score is high, THEN Visual is High
    7. IF duration is high AND Score is low, THEN Visual is Low
    8. IF duration is high AND Score is medium, THEN Visual is Medium
    9. IF duration is high AND Score is high, THEN Visual is Medium


    Rule application
    ----------------
    """


    # We need the activation of our fuzzy membership functions at these values.
    # The exact values 65 and 111 do not exist on our universes...
    # This is what fuzz.interp_membership exists for!
    score_level_lo = fuzz.interp_membership(visualScore, avg_score_lo, v_score)
    score_level_md = fuzz.interp_membership(visualScore, avg_score_md, v_score)
    score_level_hi = fuzz.interp_membership(visualScore, avg_score_hi, v_score)

    avg_duration_level_lo = fuzz.interp_membership(visualDuration, avg_duration_lo, v_duration)
    avg_duration_level_md = fuzz.interp_membership(visualDuration, avg_duration_md, v_duration)
    avg_duration_level_hi = fuzz.interp_membership(visualDuration, avg_duration_hi, v_duration)

    # Rule 1 concerns duration is low OR Score is low. (VISUAL = MEDIUM)
    active_rule1 = np.fmax(score_level_lo, avg_duration_level_lo)

    # Rule 2 concerns duration is low AND Score is medium. (VISUAL = MEDIUM)
    active_rule2 = np.fmax(score_level_md, avg_duration_level_lo)

    # Rule 3 concerns duration is low AND Score is high.
    active_rule3 = np.fmax(score_level_hi, avg_duration_level_lo)

    # Rule 4 concerns duration is medium AND Score is low.
    active_rule4 = np.fmax(score_level_lo, avg_duration_level_md)

    # Rule 5 concerns duration is medium AND Score is medium.
    active_rule5 = np.fmax(score_level_md, avg_duration_level_md)

    # Rule 6 concerns duration is medium AND Score is high.
    active_rule6 = np.fmax(score_level_hi, avg_duration_level_md)

    # Rule 7 concerns duration is high AND Score is low.
    active_rule7 = np.fmax(score_level_lo, avg_duration_level_hi)

    # Rule 8 concerns duration is high AND Score is medium.
    active_rule8 = np.fmax(score_level_md, avg_duration_level_hi)

    # Rule 9 concerns duration is high AND Score is high.
    active_rule9 = np.fmax(score_level_hi, avg_duration_level_hi)

    # Now we apply this by clipping the top off the corresponding output
    # membership function with `np.fmin`

    # low visual wm output:
    visual_activation1_lo = np.fmin(active_rule7, visual_lo)  # removed entirely to 0

    # medium visual WM output:
    visual_activation1_md = np.fmin(active_rule1, visual_md)
    visual_activation2_md = np.fmin(active_rule2, visual_md)
    visual_activation3_md = np.fmin(active_rule4, visual_md)
    visual_activation4_md = np.fmin(active_rule5, visual_md)
    visual_activation5_md = np.fmin(active_rule8, visual_md)
    visual_activation6_md = np.fmin(active_rule9, visual_md)

    # high visual WM output:
    visual_activation1_hi = np.fmin(active_rule3, visual_hi)
    visual_activation2_hi = np.fmin(active_rule6, visual_hi)

    visual0 = np.zeros_like(visual)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.fill_between(visual, visual0, visual_activation1_lo, facecolor='b', alpha=0.7)
    ax0.plot(visual, visual_lo, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(visual, visual0, visual_activation1_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation2_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation3_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation4_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation5_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation6_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')

    ax0.fill_between(visual, visual0, visual_activation1_hi, facecolor='r', alpha=0.7)
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, visual_activation2_hi, facecolor='r', alpha=0.7)
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')

    ax0.set_title('Output membership activity')

    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_visual_graph:
        plt.tight_layout()

    """
    Rule aggregation
    ----------------

    With the *activity* of each output membership function known, all output
    membership functions must be combined. This is typically done using a
    maximum operator. This step is also known as *aggregation*.

    Defuzzification
    ---------------
    Finally, to get a real world answer, we return to *crisp* logic from the
    world of fuzzy membership functions and the centroid method will be used.

    ---------------------------------
    """

    # # Aggregate all the output membership functions together
    aggregated = np.fmax(visual_activation1_lo,
                         np.fmax(visual_activation1_md, visual_activation2_md))
    aggregated1 = np.fmax(visual_activation3_md,
                          np.fmax(visual_activation4_md, aggregated))
    aggregated2 = np.fmax(visual_activation5_md,
                          np.fmax(visual_activation6_md, aggregated1))
    aggregated3 = np.fmax(visual_activation1_hi,
                          np.fmax(visual_activation2_hi, aggregated2))

    # # Calculate defuzzified result
    visual_result = fuzz.defuzz(visual, aggregated3, 'centroid')
    visual_activation = fuzz.interp_membership(visual, aggregated3, visual_result)  # for plot
    print("Visual Working Memory result: ", visual_result)

    # # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.plot(visual, visual_lo, 'b', linewidth=0.5, linestyle='--', )
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, visual0, aggregated3, facecolor='Orange', alpha=0.7)
    ax0.plot([visual_result, visual_result], [0, visual_activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Aggregated membership and result (line)')

    # # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_visual_graph:
        plt.tight_layout()
        plt.show()

    return visual_result


"""
====================================================================================
                        Calculating Auditory Working Memory
====================================================================================
"""

# from API import auditory_score_in, auditory_duration_in
# show_graph tu in boolean and in API.py(line 22, 23 and 24) for now is already set to False sbb belum nak view graph lagi

def calcAuditory(auditory_score_in, auditory_duration_in, show_auditory_graph):
    # Generate universe variables
    #  *Auditory WM  has a range of [0, 25] in units of percentage points
    a_score = auditory_score_in
    a_duration = auditory_duration_in
    auditoryScore = np.arange(0, 100, 1)
    auditoryDuration = np.arange(0, 61, 1)
    auditory = np.arange(0, 21, 1)

    # Generate fuzzy membership functions
    avg_score_lo = fuzz.trapmf(auditoryScore, [0, 0, 20, 40])
    avg_score_md = fuzz.trapmf(auditoryScore, [20, 40, 60, 80])
    avg_score_hi = fuzz.trapmf(auditoryScore, [60, 80, 100, 120])

    avg_duration_lo = fuzz.trapmf(auditoryDuration, [0, 0, 10, 20])
    avg_duration_md = fuzz.trapmf(auditoryDuration, [10, 20, 30, 40])
    avg_duration_hi = fuzz.trapmf(auditoryDuration, [30, 40, 50, 60])

    auditory_lo = fuzz.trapmf(auditory, [0, 0, 5, 8])
    auditory_md = fuzz.trapmf(auditory, [5, 8, 13, 16])
    auditory_hi = fuzz.trapmf(auditory, [13, 16, 20, 20])

    # Visualize these universes and membership functions
    fig2, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(auditoryScore, avg_score_lo, 'b', linewidth=1.5, label='Poor')
    ax0.plot(auditoryScore, avg_score_md, 'g', linewidth=1.5, label='Average')
    ax0.plot(auditoryScore, avg_score_hi, 'r', linewidth=1.5, label='Great')
    ax0.set_title('Accuracy Score')
    ax0.legend()

    ax1.plot(auditoryDuration, avg_duration_lo, 'b', linewidth=1.5, label='Fast')
    ax1.plot(auditoryDuration, avg_duration_md, 'g', linewidth=1.5, label='Medium')
    ax1.plot(auditoryDuration, avg_duration_hi, 'r', linewidth=1.5, label='Slow')
    ax1.set_title('Duration ')
    ax1.legend()

    # plotting graph for auditory WM:
    ax2.plot(auditory, auditory_lo, 'b', linewidth=1.5, label='Low')
    ax2.plot(auditory, auditory_md, 'g', linewidth=1.5, label='Medium')
    ax2.plot(auditory, auditory_hi, 'r', linewidth=1.5, label='High')
    ax2.set_title('Auditory Working Memory')
    ax2.legend()

    # Turn off top/right axes
    for ax in (ax0, ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_auditory_graph:
        plt.tight_layout()

    score_level_lo = fuzz.interp_membership(auditoryScore, avg_score_lo, a_score)
    score_level_md = fuzz.interp_membership(auditoryScore, avg_score_md, a_score)
    score_level_hi = fuzz.interp_membership(auditoryScore, avg_score_hi, a_score)

    duration_level_lo = fuzz.interp_membership(auditoryDuration, avg_duration_lo, a_duration)
    duration_level_md = fuzz.interp_membership(auditoryDuration, avg_duration_md, a_duration)
    duration_level_hi = fuzz.interp_membership(auditoryDuration, avg_duration_hi, a_duration)

    # Application of the IF THEN rules below. Rule 1 concerns low scores OR short duration.
    # The OR operator means we take the maximum of these two.
    # Rule 1 concerns duration is low OR Score is low.
    active_rule1 = np.fmax(score_level_lo, duration_level_lo)

    # Rule 2 concerns duration is low AND Score is medium.
    active_rule2 = np.fmax(score_level_md, duration_level_lo)

    # Rule 3 concerns duration is low AND Score is high.
    active_rule3 = np.fmax(score_level_hi, duration_level_lo)

    # Rule 4 concerns duration is medium AND Score is low.
    active_rule4 = np.fmax(score_level_lo, duration_level_md)

    # Rule 5 concerns duration is medium AND Score is medium.
    active_rule5 = np.fmax(score_level_md, duration_level_md)

    # Rule 6 concerns duration is medium AND Score is high.
    active_rule6 = np.fmax(score_level_hi, duration_level_md)

    # Rule 7 concerns duration is high AND Score is low.
    active_rule7 = np.fmax(score_level_lo, duration_level_hi)

    # Rule 8 concerns duration is high AND Score is medium.
    active_rule8 = np.fmax(score_level_md, duration_level_hi)

    # Rule 9 concerns duration is high AND Score is high.
    active_rule9 = np.fmax(score_level_hi, duration_level_hi)

    # Now we apply this by clipping the top off the corresponding output
    # membership function with `np.fmin`

    # low visual wm output:
    auditory_activation1_lo = np.fmin(active_rule7, auditory_lo)

    # medium visual WM output:
    auditory_activation1_md = np.fmin(active_rule1, auditory_md)
    auditory_activation2_md = np.fmin(active_rule2, auditory_md)
    auditory_activation3_md = np.fmin(active_rule4, auditory_md)
    auditory_activation4_md = np.fmin(active_rule5, auditory_md)
    auditory_activation5_md = np.fmin(active_rule8, auditory_md)
    auditory_activation6_md = np.fmin(active_rule9, auditory_md)

    # high visual WM output:
    auditory_activation1_hi = np.fmin(active_rule3, auditory_hi)
    auditory_activation2_hi = np.fmin(active_rule6, auditory_hi)

    auditory0 = np.zeros_like(auditory)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.fill_between(auditory, auditory0, auditory_activation1_lo, facecolor='b', alpha=0.7)
    ax0.plot(auditory, auditory_lo, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(auditory, auditory0, auditory_activation1_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation2_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation3_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation4_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation5_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation6_md, facecolor='g', alpha=0.7)
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')

    ax0.fill_between(auditory, auditory0, auditory_activation1_hi, facecolor='r', alpha=0.7)
    ax0.plot(auditory, auditory_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, auditory_activation2_hi, facecolor='r', alpha=0.7)
    ax0.plot(auditory, auditory_hi, 'r', linewidth=0.5, linestyle='--')

    ax0.set_title('Output membership activity')

    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_auditory_graph:
        plt.tight_layout()

    # # Aggregate all the output membership functions together
    aggregated = np.fmax(auditory_activation1_lo,
                         np.fmax(auditory_activation1_md, auditory_activation2_md))
    aggregated1 = np.fmax(auditory_activation3_md,
                          np.fmax(auditory_activation4_md, aggregated))
    aggregated2 = np.fmax(auditory_activation5_md,
                          np.fmax(auditory_activation6_md, aggregated1))
    aggregated3 = np.fmax(auditory_activation1_hi,
                          np.fmax(auditory_activation2_hi, aggregated2))

    # # Calculate defuzzified result
    auditory_result = fuzz.defuzz(auditory, aggregated3, 'centroid')
    auditory_activation = fuzz.interp_membership(auditory, aggregated3, auditory_result)  # for plot
    print("Auditory Working Memory result: ", auditory_result)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.plot(auditory, auditory_lo, 'b', linewidth=0.5, linestyle='--', )
    ax0.plot(auditory, auditory_md, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(auditory, auditory_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(auditory, auditory0, aggregated, facecolor='Orange', alpha=0.7)
    ax0.plot([auditory_result, auditory_result], [0, auditory_activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Aggregated membership and result (line)')

    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_auditory_graph:
        plt.tight_layout()
        plt.show()

    return auditory_result

"""
=======================================================================================
                            Calculating Working Memory Index
=======================================================================================

"""

def calcWMI(visual_result, auditory_result, show_wmi_graph):
    visual = np.arange(0, 21, 1)
    auditory = np.arange(0, 21, 1)
    wmi = np.arange(0, 21, 1)

    # Generating WMI fuzzy membership functions

    visual_lo = fuzz.trapmf(visual, [0, 0, 5, 8])
    visual_md = fuzz.trapmf(visual, [5, 8, 13, 16])
    visual_hi = fuzz.trapmf(visual, [13, 16, 20, 20])

    auditory_lo = fuzz.trapmf(auditory, [0, 0, 5, 8])
    auditory_md = fuzz.trapmf(auditory, [5, 8, 13, 16])
    auditory_hi = fuzz.trapmf(auditory, [13, 16, 20, 20])

    wmi_lo = fuzz.trapmf(wmi, [0, 0, 5, 8])
    wmi_md = fuzz.trapmf(wmi, [5, 8, 13, 16])
    wmi_hi = fuzz.trapmf(wmi, [13, 16, 20, 20])

    # Visualize these universes and membership functions
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(visual, visual_lo, 'b', linewidth=1.5, label='Poor')
    ax0.plot(visual, visual_md, 'g', linewidth=1.5, label='Average')
    ax0.plot(visual, visual_hi, 'r', linewidth=1.5, label='Great')
    ax0.set_title('Visual WM ')
    ax0.legend()

    ax1.plot(auditory, auditory_lo, 'b', linewidth=1.5, label='Slow')
    ax1.plot(auditory, auditory_md, 'g', linewidth=1.5, label='Acceptable')
    ax1.plot(auditory, auditory_hi, 'r', linewidth=1.5, label='Fast')
    ax1.set_title('Auditory WM')
    ax1.legend()

    ax2.plot(wmi, visual_lo, 'b', linewidth=1.5, label='Low')
    ax2.plot(wmi, visual_md, 'g', linewidth=1.5, label='Medium')
    ax2.plot(wmi, visual_hi, 'r', linewidth=1.5, label='High')
    ax2.set_title('Working Memory Index')
    ax2.legend()

    # Turn off top/right axes
    for ax in (ax0, ax1, ax2):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_wmi_graph:
        plt.tight_layout()

    visual_level_lo = fuzz.interp_membership(visual, visual_lo, visual_result)
    visual_level_md = fuzz.interp_membership(visual, visual_md, visual_result)
    visual_level_hi = fuzz.interp_membership(visual, visual_hi, visual_result)

    auditory_level_lo = fuzz.interp_membership(auditory, auditory_lo, auditory_result)
    auditory_level_md = fuzz.interp_membership(auditory, auditory_md, auditory_result)
    auditory_level_hi = fuzz.interp_membership(auditory, auditory_hi, auditory_result)

    # The OR operator means we take the maximum of these two.
    active_rule1 = np.fmax(visual_level_lo, auditory_level_lo)

    # Rule 2 concerns Auditory is low AND Visual is medium. (VISUAL = MEDIUM)
    active_rule2 = np.fmax(visual_level_md, auditory_level_lo)

    # Rule 3 concerns Auditory is low AND Visual is high.
    active_rule3 = np.fmax(visual_level_hi, auditory_level_lo)

    # Rule 4 concerns Auditory is medium AND Visual is low.
    active_rule4 = np.fmax(visual_level_lo, auditory_level_md)

    # Rule 5 concerns Auditory is medium AND Visual is medium.
    active_rule5 = np.fmax(visual_level_md, auditory_level_md)

    # Rule 6 concerns Auditory is medium AND Visual is high.
    active_rule6 = np.fmax(visual_level_hi, auditory_level_md)

    # Rule 7 concerns Auditory is high AND Visual is low.
    active_rule7 = np.fmax(visual_level_lo, auditory_level_hi)

    # Rule 8 concerns Auditory is high AND Visual is medium.
    active_rule8 = np.fmax(visual_level_md, auditory_level_hi)

    # Rule 9 concerns Auditory is high AND Visual is high.
    active_rule9 = np.fmax(visual_level_hi, auditory_level_hi)

    # Now we apply this by clipping the top off the corresponding output
    # membership function with `np.fmin`
    # low WMI output:
    wmi_activation1_lo = np.fmin(active_rule7, wmi_lo)  # removed entirely to 0

    # medium WMI output:
    wmi_activation1_md = np.fmin(active_rule1, wmi_md)
    wmi_activation2_md = np.fmin(active_rule2, wmi_md)
    wmi_activation3_md = np.fmin(active_rule4, wmi_md)
    wmi_activation4_md = np.fmin(active_rule5, wmi_md)
    wmi_activation5_md = np.fmin(active_rule8, wmi_md)
    wmi_activation6_md = np.fmin(active_rule9, wmi_md)

    # high WMI output:
    wmi_activation1_hi = np.fmin(active_rule3, wmi_hi)
    wmi_activation2_hi = np.fmin(active_rule6, wmi_hi)
    wmi0 = np.zeros_like(wmi)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.fill_between(visual, wmi0, wmi_activation1_lo, facecolor='b', alpha=0.7)
    ax0.plot(visual, visual_lo, 'b', linewidth=0.5, linestyle='--', )

    ax0.fill_between(visual, wmi0, wmi_activation1_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation2_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation2_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation3_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation4_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation5_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation6_md, facecolor='g', alpha=0.7)
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')

    ax0.fill_between(visual, wmi0, wmi_activation1_hi, facecolor='r', alpha=0.7)
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, wmi_activation2_hi, facecolor='r', alpha=0.7)
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')

    ax0.set_title('Output membership activity')

    # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_wmi_graph:
        plt.tight_layout()

    """
    .. image:: PLOT2RST.current_figure

    Rule aggregation
    ----------------

    With the *activity* of each output membership function known, all output
    membership functions must be combined. This is typically done using a
    maximum operator. This step is also known as *aggregation*.

    Defuzzification
    ---------------
    Finally, to get a real world answer, we return to *crisp* logic from the
    world of fuzzy membership functions. For the purposes of this example
    the centroid method will be used.

    The result is a tip of **20.2%**.
    ---------------------------------
    """

    # Aggregate all the output membership functions together
    aggregated = np.fmax(wmi_activation1_lo,
                         np.fmax(wmi_activation1_md, wmi_activation2_md))
    aggregated1 = np.fmax(wmi_activation3_md,
                          np.fmax(wmi_activation4_md, aggregated))
    aggregated2 = np.fmax(wmi_activation5_md,
                          np.fmax(wmi_activation6_md, aggregated1))
    aggregated3 = np.fmax(wmi_activation1_hi,
                          np.fmax(wmi_activation2_hi, aggregated2))

    # Calculate defuzzified result
    wmi_result = fuzz.defuzz(wmi, aggregated3, 'centroid')
    wmi_activation = fuzz.interp_membership(wmi, aggregated3, wmi_result)  # for plot
    print("Working Memory Index result: ", wmi_result)

    # Visualize this
    fig, ax0 = plt.subplots(figsize=(8, 3))

    ax0.plot(visual, visual_lo, 'b', linewidth=0.5, linestyle='--', )
    ax0.plot(visual, visual_md, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(visual, visual_hi, 'r', linewidth=0.5, linestyle='--')
    ax0.fill_between(visual, wmi0, aggregated3, facecolor='Orange', alpha=0.7)
    ax0.plot([wmi_result, wmi_result], [0, wmi_activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Aggregated membership and result (line)')

    # # Turn off top/right axes
    for ax in (ax0,):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    if show_wmi_graph:
        plt.tight_layout()
        plt.show()

    return wmi_result





