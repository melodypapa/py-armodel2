"""Example: Using Builder Classes to Create AUTOSAR Data Types.

This example demonstrates how to use the Builder classes to create AUTOSAR data types.
The Builder classes provide a clean pattern for object creation, even though they're
currently simple (they create instances without fluent method chaining).

The example creates:
- Base Types (float32, float64, sint16, sint32, sint8, uint16, uint32, uint8, void)
- Compu Methods (boolean_Literals)
- Data Constraints (for signed/unsigned integers)
- Implementation Data Types

Note:
- Builder classes in py-armodel2 are currently simple - they create instances and return them.
- Attributes still need to be set directly on the objects after creation.
- Builder classes provide a clean separation of object creation logic.
"""

from armodel.models import (
    # AUTOSAR Core
    AUTOSAR,
    AUTOSARBuilder,
    ARPackage,
    ARPackageBuilder,
    ARRef,
    ImplementationDataType,
    ImplementationDataTypeBuilder,
    # MSR - Base Types
    SwBaseType,
    SwBaseTypeBuilder,
    BaseTypeDirectDefinition,
    # MSR - Computation Method
    CompuMethod,
    CompuMethodBuilder,
    Compu,
    CompuBuilder,
    CompuScales,
    CompuScalesBuilder,
    CompuScale,
    CompuScaleBuilder,
    CompuConst,
    CompuConstBuilder,
    CompuScaleConstantContents,
    CompuScaleConstantContentsBuilder,
    CompuConstTextContent,
    CompuConstTextContentBuilder,
    # MSR - Constraints
    DataConstr,
    DataConstrBuilder,
    InternalConstrs,
    DataConstrRule,
    # MSR - Data Dictionary
    SwDataDefProps,
    # Primitive Types
    Limit,
    IntervalTypeEnum,
    VerbatimString,
)

from armodel.writer import ARXMLWriter


# ============================================================================
# Helper Functions
# ============================================================================

def create_base_type(name: str, size: int, encoding: str, mem_align: int = None, native: str = None) -> SwBaseType:
    """Create a base type using Builder pattern.

    Args:
        name: Short name for the base type
        size: Base type size in bits
        encoding: Base type encoding
        mem_align: Memory alignment (optional)
        native: Native declaration (optional)

    Returns:
        SwBaseType instance
    """
    builder = SwBaseTypeBuilder()
    base_type = builder.build()
    base_type.short_name = name
    base_type.category = "FIXED_LENGTH"
    base_type.base_type_definition = BaseTypeDirectDefinition()
    base_type.base_type_definition.base_type_size = size
    base_type.base_type_definition.base_type_encoding = encoding
    if mem_align is not None:
        base_type.base_type_definition.mem_alignment = mem_align
    if native is not None:
        base_type.base_type_definition.native = native
    return base_type


def create_compu_scale_with_const(value: str, text_value: str) -> CompuScale:
    """Create a CompuScale with CompuConst using Builders.

    Args:
        value: The numeric value for the scale
        text_value: The text value for the CompuConst

    Returns:
        CompuScale instance
    """
    scale_builder = CompuScaleBuilder()
    scale = scale_builder.build()
    scale.lower_limit = Limit(value=value, interval_type=IntervalTypeEnum.CLOSED)
    scale.upper_limit = Limit(value=value, interval_type=IntervalTypeEnum.CLOSED)

    # Create CompuConst using Builder
    compu_const_builder = CompuConstBuilder()
    compu_const = compu_const_builder.build()

    # Create CompuConstTextContent using Builder
    compu_const_text_builder = CompuConstTextContentBuilder()
    compu_const_text = compu_const_text_builder.build()
    compu_const_text.vt = VerbatimString(value=text_value)
    compu_const.compu_const_content_type = compu_const_text

    # Create CompuScaleConstantContents using Builder
    scale_contents_builder = CompuScaleConstantContentsBuilder()
    scale_contents = scale_contents_builder.build()
    scale_contents.compu_const = compu_const

    scale.compu_scale_contents = scale_contents
    return scale


def create_data_constr_with_builder(name: str, lower: int, upper: int) -> DataConstr:
    """Create a data constraint using Builder pattern.

    Args:
        name: Short name for the data constraint
        lower: Lower limit value
        upper: Upper limit value

    Returns:
        DataConstr instance
    """
    data_constr_builder = DataConstrBuilder()
    data_constr = data_constr_builder.build()
    data_constr.short_name = name

    # Create InternalConstrs
    internal_constrs = InternalConstrs()
    internal_constrs.lower_limit = Limit(value=str(lower), interval_type=IntervalTypeEnum.CLOSED)
    internal_constrs.upper_limit = Limit(value=str(upper), interval_type=IntervalTypeEnum.CLOSED)

    # Create DataConstrRule
    data_constr_rule = DataConstrRule()
    data_constr_rule.internal_constrs = internal_constrs

    data_constr.data_constr_rules = [data_constr_rule]
    return data_constr


def create_value_impl_data_type_with_builder(
    name: str,
    base_type_ref_path: str,
    data_constr_ref_path: str = None,
) -> ImplementationDataType:
    """Create an implementation data type with VALUE category using Builder.

    Args:
        name: Short name for the implementation data type
        base_type_ref_path: Path to the base type reference
        data_constr_ref_path: Optional path to the data constraint reference

    Returns:
        ImplementationDataType instance
    """
    builder = ImplementationDataTypeBuilder()
    impl_data_type = builder.build()
    impl_data_type.short_name = name
    impl_data_type.category = "VALUE"
    impl_data_type.type_emitter = "BSW"

    # Create sw_data_def_props
    sw_data_def_props = SwDataDefProps()

    # Create base_type_ref
    base_type_ref = ARRef(
        dest="SW-BASE-TYPE",
        value=base_type_ref_path,
    )
    sw_data_def_props.base_type_ref = base_type_ref

    # Create data_constr_ref if provided
    if data_constr_ref_path:
        data_constr_ref = ARRef(
            dest="DATA-CONSTR",
            value=data_constr_ref_path,
        )
        sw_data_def_props.data_constr_ref = data_constr_ref

    impl_data_type.sw_data_def_props = sw_data_def_props
    return impl_data_type


def create_type_ref_impl_data_type_with_builder(
    name: str,
    impl_data_type_ref_path: str,
) -> ImplementationDataType:
    """Create an implementation data type with TYPE_REFERENCE category using Builder.

    Args:
        name: Short name for the implementation data type
        impl_data_type_ref_path: Path to the implementation data type reference

    Returns:
        ImplementationDataType instance
    """
    builder = ImplementationDataTypeBuilder()
    impl_data_type = builder.build()
    impl_data_type.short_name = name
    impl_data_type.category = "TYPE_REFERENCE"
    impl_data_type.type_emitter = "BSW"

    # Create sw_data_def_props
    sw_data_def_props = SwDataDefProps()

    # Create implementation_data_type_ref
    impl_data_type_ref = ARRef(
        dest="IMPLEMENTATION-DATA-TYPE",
        value=impl_data_type_ref_path,
    )
    sw_data_def_props.implementation_data_type_ref = impl_data_type_ref

    impl_data_type.sw_data_def_props = sw_data_def_props
    return impl_data_type


def create_autosar_datatypes_with_builders() -> AUTOSAR:
    """Create AUTOSAR data types using Builder classes.

    Returns:
        AUTOSAR instance with platform data types
    """
    # Create AUTOSAR using Builder
    autosar_builder = AUTOSARBuilder()
    autosar = autosar_builder.build()
    autosar.clear()

    # ========================================================================
    # Root Package: AUTOSAR_Platform
    # ========================================================================
    root_pkg_builder = ARPackageBuilder()
    root_pkg = root_pkg_builder.build()
    root_pkg.short_name = "AUTOSAR_Platform"

    # ========================================================================
    # Sub-package: BaseTypes
    # ========================================================================
    base_types_pkg_builder = ARPackageBuilder()
    base_types_pkg = base_types_pkg_builder.build()
    base_types_pkg.short_name = "BaseTypes"
    base_types_pkg.category = "STANDARD"

    # Create all base types using helper function
    base_types_pkg.elements.extend([
        create_base_type("float32", 32, "IEEE754", 32, "float"),
        create_base_type("float64", 64, "IEEE754", 64, "double"),
        create_base_type("sint16", 16, "2C", 16, "short"),
        create_base_type("sint16_least", 32, "2C", 32, "signed int"),
        create_base_type("sint32", 32, "2C", 32, "int"),
        create_base_type("sint32_least", 32, "2C", 32, "signed int"),
        create_base_type("sint8", 8, "2C", 8, "signed char"),
        create_base_type("sint8_least", 32, "2C", 32, "signed int"),
        create_base_type("uint16", 16, "NONE", 16, "unsigned short"),
        create_base_type("uint16_least", 32, "NONE", 32, "unsigned int"),
        create_base_type("uint32", 32, "NONE", 32, "unsigned int"),
        create_base_type("uint32_least", 32, "NONE", 32, "unsigned int"),
        create_base_type("uint8", 8, "NONE", 8, "unsigned char"),
        create_base_type("uint8_least", 32, "NONE", 32, "unsigned int"),
        create_base_type("void", 32, "VOID", None, "void"),
    ])

    # ========================================================================
    # Sub-package: CompuMethods
    # ========================================================================
    compu_methods_pkg_builder = ARPackageBuilder()
    compu_methods_pkg = compu_methods_pkg_builder.build()
    compu_methods_pkg.short_name = "CompuMethods"
    compu_methods_pkg.category = "STANDARD"

    # Create boolean_Literals CompuMethod using Builders
    boolean_literals_builder = CompuMethodBuilder()
    boolean_literals = boolean_literals_builder.build()
    boolean_literals.short_name = "boolean_Literals"
    boolean_literals.category = "TEXTTABLE"

    # Create compu_internal_to_phys using Builder
    compu_builder = CompuBuilder()
    compu_internal_to_phys = compu_builder.build()

    # Create compu_scales using Builder
    compu_scales_builder = CompuScalesBuilder()
    compu_scales = compu_scales_builder.build()

    # Create scales for FALSE and TRUE
    compu_scales.compu_scales = [
        create_compu_scale_with_const("0", "FALSE"),
        create_compu_scale_with_const("1", "TRUE"),
    ]

    # Assemble CompuMethod
    compu_internal_to_phys.compu_content = compu_scales
    boolean_literals.compu_internal_to_phys = compu_internal_to_phys

    compu_methods_pkg.elements.append(boolean_literals)

    # ========================================================================
    # Sub-package: DataConstrs
    # ========================================================================
    data_constrs_pkg_builder = ARPackageBuilder()
    data_constrs_pkg = data_constrs_pkg_builder.build()
    data_constrs_pkg.short_name = "DataConstrs"
    data_constrs_pkg.category = "STANDARD"

    # Create data constraints using helper function
    data_constrs_pkg.elements.extend([
        create_data_constr_with_builder("sint16", -32768, 32767),
        create_data_constr_with_builder("sint16_least", -32768, 32767),
        create_data_constr_with_builder("sint32", -2147483648, 2147483647),
        create_data_constr_with_builder("sint32_least", -2147483648, 2147483647),
        create_data_constr_with_builder("sint8", -128, 127),
        create_data_constr_with_builder("sint8_least", -128, 127),
        create_data_constr_with_builder("uint16", 0, 65535),
        create_data_constr_with_builder("uint16_least", 0, 65535),
        create_data_constr_with_builder("uint32", 0, 4294967295),
        create_data_constr_with_builder("uint32_least", 0, 4294967295),
        create_data_constr_with_builder("uint8", 0, 255),
        create_data_constr_with_builder("uint8_least", 0, 255),
    ])

    # ========================================================================
    # Sub-package: ImplementationDataTypes
    # ========================================================================
    impl_data_types_pkg_builder = ARPackageBuilder()
    impl_data_types_pkg = impl_data_types_pkg_builder.build()
    impl_data_types_pkg.short_name = "ImplementationDataTypes"
    impl_data_types_pkg.category = "STANDARD"

    # Create implementation data types using helper functions
    impl_data_types_pkg.elements.extend([
        # Boolean (type reference to uint8)
        create_type_ref_impl_data_type_with_builder(
            "boolean",
            "/AUTOSAR_Platform1/ImplementationDataTypes/uint8",
        ),
        # Float types (value category)
        create_value_impl_data_type_with_builder(
            "float32",
            "/AUTOSAR_Platform1/BaseTypes/float32",
        ),
        create_value_impl_data_type_with_builder(
            "float64",
            "/AUTOSAR_Platform1/BaseTypes/float64",
        ),
        # Signed integer types (value category with data constraints)
        create_value_impl_data_type_with_builder(
            "sint16",
            "/AUTOSAR_Platform1/BaseTypes/sint16",
            "/AUTOSAR_Platform1/DataConstrs/sint16",
        ),
        create_value_impl_data_type_with_builder(
            "sint16_least",
            "/AUTOSAR_Platform1/BaseTypes/sint16_least",
            "/AUTOSAR_Platform1/DataConstrs/sint16_least",
        ),
        create_value_impl_data_type_with_builder(
            "sint32",
            "/AUTOSAR_Platform1/BaseTypes/sint32",
            "/AUTOSAR_Platform1/DataConstrs/sint32",
        ),
        create_value_impl_data_type_with_builder(
            "sint32_least",
            "/AUTOSAR_Platform1/BaseTypes/sint32_least",
            "/AUTOSAR_Platform1/DataConstrs/sint32_least",
        ),
        create_value_impl_data_type_with_builder(
            "sint8",
            "/AUTOSAR_Platform1/BaseTypes/sint8",
            "/AUTOSAR_Platform1/DataConstrs/sint8",
        ),
        create_value_impl_data_type_with_builder(
            "sint8_least",
            "/AUTOSAR_Platform1/BaseTypes/sint8_least",
            "/AUTOSAR_Platform1/DataConstrs/sint8_least",
        ),
        # Unsigned integer types (value category with data constraints)
        create_value_impl_data_type_with_builder(
            "uint16",
            "/AUTOSAR_Platform1/BaseTypes/uint16",
            "/AUTOSAR_Platform1/DataConstrs/uint16",
        ),
        create_value_impl_data_type_with_builder(
            "uint16_least",
            "/AUTOSAR_Platform1/BaseTypes/uint16_least",
            "/AUTOSAR_Platform1/DataConstrs/uint16_least",
        ),
        create_value_impl_data_type_with_builder(
            "uint32",
            "/AUTOSAR_Platform1/BaseTypes/uint32",
            "/AUTOSAR_Platform1/DataConstrs/uint32",
        ),
        create_value_impl_data_type_with_builder(
            "uint32_least",
            "/AUTOSAR_Platform1/BaseTypes/uint32_least",
            "/AUTOSAR_Platform1/DataConstrs/uint32_least",
        ),
        create_value_impl_data_type_with_builder(
            "uint8",
            "/AUTOSAR_Platform1/BaseTypes/uint8",
            "/AUTOSAR_Platform1/DataConstrs/uint8",
        ),
        create_value_impl_data_type_with_builder(
            "uint8_least",
            "/AUTOSAR_Platform1/BaseTypes/uint8_least",
            "/AUTOSAR_Platform1/DataConstrs/uint8_least",
        ),
    ])

    # ========================================================================
    # Assemble Package Hierarchy
    # ========================================================================
    root_pkg.ar_packages.extend([
        base_types_pkg,
        compu_methods_pkg,
        data_constrs_pkg,
        impl_data_types_pkg,
    ])

    # Add root package to AUTOSAR
    autosar.ar_packages.append(root_pkg)

    return autosar


def main():
    """Main function to create and save AUTOSAR data types using Builders."""
    print("=== Creating AUTOSAR Data Types using Builder Classes ===")
    print()

    # Create AUTOSAR data types programmatically using Builders
    autosar = create_autosar_datatypes_with_builders()

    print("✓ Created AUTOSAR structure:")
    print(f"  - Root packages: {len(autosar.ar_packages)}")
    if autosar.ar_packages:
        root_pkg = autosar.ar_packages[0]
        print(f"  - Root package: {root_pkg.short_name}")
        if hasattr(root_pkg, 'ar_packages'):
            print(f"  - Sub-packages: {len(root_pkg.ar_packages)}")
            for pkg in root_pkg.ar_packages:
                elem_count = len(pkg.elements) if hasattr(pkg, 'elements') else 0
                print(f"    - {pkg.short_name}: {elem_count} elements")

    print()

    # Save to ARXML file
    writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
    output_file = "output_builder_classes.arxml"
    writer.save_arxml(output_file)
    print(f"✓ Saved to {output_file}")

    print()
    print("✓ All operations completed successfully!")


if __name__ == "__main__":
    main()