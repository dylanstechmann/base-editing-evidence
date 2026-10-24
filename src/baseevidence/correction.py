"""Classify a declared pathogenic-to-corrected direction without guide design."""

from baseevidence.audit import substitution

CLASSICAL_DIRECTION = {
    "classical_ABE_conversion_class_only": "classical_ABE_chemistry_direction",
    "classical_CBE_conversion_class_only": "classical_CBE_chemistry_direction",
}


def correction(pathogenic, corrected, *, coordinate_system):
    """Classical ABE/CBE direction of a declared single-base correction.

    Complementary corrections share a chemistry direction. No PAM, sequence
    window, bystander, delivery, editor-efficiency or clinical inference is
    performed; transversions stay outside both classical classes.
    """
    conversion = substitution(pathogenic, corrected, coordinate_system=coordinate_system)
    if conversion == "no_sequence_change":
        direction, change_type, interpretation = None, "no_sequence_change", (
            "A correction requires a sequence change; identical bases declare none.")
    elif conversion in CLASSICAL_DIRECTION:
        direction, change_type = CLASSICAL_DIRECTION[conversion], "transition"
        interpretation = (
            "A classical conversion direction covers this change. Direction membership establishes "
            "no targetable site, PAM context, editing window, intended-only product, efficiency or tissue function.")
    else:
        direction, change_type = None, "transversion"
        interpretation = (
            "A transversion is outside both classical conversion classes. Broader-change machinery "
            "such as prime editing is a separate method comparison, not a designed or selected intervention here.")
    return {"pathogenic_base": pathogenic, "corrected_base": corrected,
            "coordinate_system": coordinate_system, "conversion_class": conversion,
            "change_type": change_type, "within_classical_chemistry": conversion in CLASSICAL_DIRECTION,
            "classical_chemistry_direction": direction,
            "functional_rescue_inferred": False, "clinical_protocol_provided": False,
            "interpretation": interpretation}