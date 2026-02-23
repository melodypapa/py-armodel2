"""Code generation functions for AUTOSAR models."""

from typing import Any, Dict, List, Optional, Set, Union

from ._common import (
    get_python_identifier,
    get_python_identifier_with_ref,
    to_snake_case,
    to_autosar_xml_format,
)
from .type_utils import (
    detect_circular_import,
    get_python_type,
    get_type_import_path,
    get_type_package_path,
    is_primitive_type,
    is_enum_type,
    extract_base_type,
    extract_attribute_metadata,
    get_type_coercion_function,
    should_apply_type_coercion,
)


# Base class names for AUTOSAR primitives and enums
PRIMITIVE_BASE_CLASS = "ARPrimitive"
ENUM_BASE_CLASS = "AREnum"


def generate_class_code(
    type_def: Dict[str, Any],
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    include_members: bool = False,
    json_file_path: str = "",
    dependency_graph: Optional[Dict[str, Set[str]]] = None,
    force_type_checking_imports: Optional[Dict[str, Union[List[str], str]]] = None,
    builder_imports: str = "",
) -> str:
    """Generate Python class code from type definition.

    Args:
        type_def: Type definition from mapping.json
        hierarchy_info: Dictionary with parent and abstract information from hierarchy.json
        package_data: Dictionary with package data including class attributes
        include_members: Whether to include member lists from package definitions
        json_file_path: Path to the JSON file containing the class definition
        dependency_graph: Complete dependency graph for circular import detection
        force_type_checking_imports: Dict mapping class names to types that should use TYPE_CHECKING
        builder_imports: Import statements needed for Builder class (added at top of file)

    Returns:
        Generated Python code as string
    """
    if dependency_graph is None:
        dependency_graph = {}
    if force_type_checking_imports is None:
        force_type_checking_imports = {}
    class_name = type_def["name"]
    is_splitable = type_def.get("splitable", False)
    split_file_name = type_def.get("split_file_name", "")
    package_path = type_def.get("package_path", "")

    # Get parent and abstract status from hierarchy
    parent_class = None
    is_abstract = False

    # First check hierarchy_info for parent and abstract status
    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name]["parent"]
        is_abstract = hierarchy_info[class_name]["is_abstract"]

    # Also check package_data for abstract status (takes precedence if available)
    if include_members and package_path in package_data:
        for cls in package_data[package_path].get("classes", []):
            if cls["name"] == class_name:
                # Use is_abstract from JSON if available
                if "is_abstract" in cls:
                    is_abstract = cls["is_abstract"]
                # Use parent from JSON if available
                if "parent" in cls and cls["parent"]:
                    parent_class = cls["parent"]
                break

    # Ensure ARObject is not the parent of itself
    # Default to ARObject only if class_name is not "ARObject" and no parent found
    if not parent_class and class_name != "ARObject":
        parent_class = "ARObject"
    elif parent_class == "ARObject" and class_name == "ARObject":
        # Prevent ARObject from being its own parent
        parent_class = None

    # Get class information from package_data (includes sources with PDF references)
    sources = []
    if include_members and package_path in package_data:
        for cls in package_data[package_path].get("classes", []):
            if cls["name"] == class_name:
                sources = cls.get("sources", [])
                break

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"{class_name} AUTOSAR element."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Generate class code
    if class_name == "ARObject":
        future_import = "from __future__ import annotations\n"
        type_checking_import = "from typing import TYPE_CHECKING, Optional, Union, get_type_hints, get_args, get_origin\n"
        base_import = "import xml.etree.ElementTree as ET\n"
        # Import NameConverter for reflection-based serialization
        name_converter_import = "from armodel.serialization.name_converter import NameConverter\n"
        code = f'''"""{docstring}"""

{future_import}{type_checking_import}{base_import}{name_converter_import}
'''
    else:
        # For other classes, we need to check attribute types first to determine imports
        # Collect attribute types for imports
        attribute_types = {}
        has_xml_attribute = False
        if include_members and package_path in package_data:
            class_info = package_data[package_path].get("classes", [])
            for cls in class_info:
                if cls["name"] == class_name and "attributes" in cls:
                    for attr_name, attr_info in cls["attributes"].items():
                        attr_type = attr_info["type"]
                        multiplicity = attr_info["multiplicity"]
                        is_ref = attr_info.get("is_ref", False)
                        kind = attr_info.get("kind", "attribute")
                        decorator_name = None  # Initialize decorator_name
                        attribute_types[attr_name] = {
                            "type": attr_type,
                            "multiplicity": multiplicity,
                            "is_ref": is_ref,
                            "kind": kind,
                        }
                        # Parse decorator field if present
                        if "decorator" in attr_info:
                            decorator_spec = attr_info["decorator"]
                            # Parse format: "decorator_name:param1,param2,..."
                            if ":" in decorator_spec:
                                decorator_name, params = decorator_spec.split(":", 1)
                                attribute_types[attr_name]["decorator_name"] = decorator_name
                                attribute_types[attr_name]["decorator_params"] = params
                            else:
                                decorator_name = decorator_spec
                                attribute_types[attr_name]["decorator_name"] = decorator_spec
                                attribute_types[attr_name]["decorator_params"] = None
                        # Check if this attribute uses xml_attribute (via kind or decorator)
                        if kind == "xml_attribute" or decorator_name == "xml_attribute":
                            has_xml_attribute = True
                        else:
                            # Auto-detect YS→IES pattern and add xml_element_name decorator
                            # Check if attribute name ends with "ies" and multiplicity is "*"
                            if (
                                attr_name.lower().endswith("ies")
                                and attr_info.get("multiplicity") == "*"
                            ):
                                # Convert attribute name to XML tag
                                snake_name = to_snake_case(attr_name)
                                xml_tag = snake_name.upper().replace("_", "-")
                                # Convert IES to YS (e.g., ENTITIES → ENTITYS)
                                legacy_tag = f"{xml_tag[:-3]}YS"
                                attribute_types[attr_name]["decorator_name"] = "xml_element_name"
                                attribute_types[attr_name]["decorator_params"] = legacy_tag
                    break

        # Check if we need Any type
        uses_any_type = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                attr_type = attr_info["type"]
                if attr_type.startswith("any ("):
                    uses_any_type = True
                    break

        # Build imports based on what we need
        future_import = "from __future__ import annotations\n"
        if uses_any_type:
            basic_import = "from typing import TYPE_CHECKING, Optional, Any\n"
        else:
            basic_import = "from typing import TYPE_CHECKING, Optional\n"
        base_import = "import xml.etree.ElementTree as ET\n"

        # Add xml_attribute import if needed
        decorator_import = ""
        if has_xml_attribute:
            decorator_import = "from armodel.serialization.decorators import xml_attribute\n"

        # Check if this class has xml_element_name decorators
        has_xml_element_name = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                decorator_name = attr_info.get("decorator_name")
                if decorator_name == "xml_element_name":
                    has_xml_element_name = True
                    break
        if has_xml_element_name:
            decorator_import += "from armodel.serialization.decorators import xml_element_name\n"

        # Check if this class uses atpVariation pattern
        atp_type = type_def.get("atp_type", None)
        if atp_type == "atpVariation":
            decorator_import += "from armodel.serialization.decorators import atp_variant\n"

        # Check if this class has lang_prefix attributes
        has_lang_prefix = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                decorator_name = attr_info.get("decorator_name")
                if decorator_name == "lang_prefix":
                    has_lang_prefix = True
                    break
        if has_lang_prefix:
            decorator_import += "from armodel.serialization.decorators import lang_prefix\n"

        # Check if this class has lang_abbr decorators
        has_lang_abbr = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                decorator_name = attr_info.get("decorator_name")
                if decorator_name == "lang_abbr":
                    has_lang_abbr = True
                    break
        if has_lang_abbr:
            decorator_import += "from armodel.serialization.decorators import lang_abbr\n"

        # Check if this class has ref_conditional decorators
        has_ref_conditional = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                decorator_name = attr_info.get("decorator_name")
                if decorator_name == "ref_conditional":
                    has_ref_conditional = True
                    break
        if has_ref_conditional:
            decorator_import += "from armodel.serialization.decorators import ref_conditional\n"

        # Check if this class has instance_ref decorators
        has_instance_ref = False
        if attribute_types:
            for attr_name, attr_info in attribute_types.items():
                decorator_name = attr_info.get("decorator_name")
                if decorator_name == "instance_ref":
                    has_instance_ref = True
                    break
        if has_instance_ref:
            decorator_import += "from armodel.serialization.decorators import instance_ref\n"
            decorator_import += "from armodel.serialization.decorators import ref_conditional\n"

        code = f'''"""{docstring}"""

{future_import}{basic_import}{base_import}{decorator_import}
'''

    # Add parent class import
    if parent_class and parent_class != "ARObject":
        # Find parent class path from hierarchy or mapping
        parent_import = get_type_import_path(parent_class, package_data)
        if parent_import:
            code += f"{parent_import}\n"
        else:
            # Fallback to ARObject import
            code += "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject\n"

    # Add Builder imports at the top (after all other imports to avoid E402 errors)
    # Deduplicate imports to avoid F811 redefinition errors
    if builder_imports:
        # Split builder imports into lines and check each one
        for builder_import_line in builder_imports.strip().split("\n"):
            # Skip empty lines
            if not builder_import_line.strip():
                continue

            # Check if the exact import line already exists
            if builder_import_line in code:
                continue

            # For 'from X import Y' statements, check for partial duplicates
            # Example: "from abc import ABC, abstractmethod" when "from abc import ABC" exists
            if " import " in builder_import_line:
                import_parts = builder_import_line.split(" import ")
                if len(import_parts) == 2:
                    source = import_parts[0].replace("from ", "").strip()
                    items = [item.strip() for item in import_parts[1].split(",")]

                    # Check if items are already imported from this source
                    # We need to find existing imports from the same source
                    existing_import_pattern = f"from {source} import "
                    if existing_import_pattern in code:
                        # Extract all items already imported from this source
                        import_start = code.find(existing_import_pattern)
                        import_end = code.find("\n", import_start)
                        existing_import = code[import_start:import_end]

                        # Parse existing import to get already imported items
                        existing_items_str = existing_import.split(" import ")[1].strip()
                        existing_items = [item.strip() for item in existing_items_str.split(",")]

                        # Find which items are not yet imported
                        new_items = [item for item in items if item not in existing_items]

                        if new_items:
                            # Add only the new items
                            code += f"from {source} import {', '.join(new_items)}\n"
                        # If all items already exist, skip this import
                        continue

            # Not a duplicate, add the full import line
            code += builder_import_line + "\n"

    # Collect attribute types for all classes
    attribute_types = {}
    if include_members and package_path in package_data:
        class_info = package_data[package_path].get("classes", [])
        for cls in class_info:
            if cls["name"] == class_name and "attributes" in cls:
                for attr_name, attr_info in cls["attributes"].items():
                    attr_type = attr_info["type"]
                    multiplicity = attr_info["multiplicity"]
                    is_ref = attr_info.get("is_ref", False)
                    kind = attr_info.get("kind", "attribute")
                    attribute_types[attr_name] = {
                        "type": attr_type,
                        "multiplicity": multiplicity,
                        "is_ref": is_ref,
                        "kind": kind,
                    }
                    # Parse decorator field if present
                    if "decorator" in attr_info:
                        decorator_spec = attr_info["decorator"]
                        # Parse format: "decorator_name:param1,param2,..."
                        if ":" in decorator_spec:
                            decorator_name, params = decorator_spec.split(":", 1)
                            attribute_types[attr_name]["decorator_name"] = decorator_name
                            attribute_types[attr_name]["decorator_params"] = params
                        else:
                            attribute_types[attr_name]["decorator_name"] = decorator_spec
                            attribute_types[attr_name]["decorator_params"] = None
                    else:
                        # Auto-detect YS→IES pattern and add xml_element_name decorator
                        # Check if attribute name ends with "ies" and multiplicity is "*"
                        if (
                            attr_name.lower().endswith("ies")
                            and attr_info.get("multiplicity") == "*"
                        ):
                            # Convert attribute name to XML tag
                            snake_name = to_snake_case(attr_name)
                            xml_tag = snake_name.upper().replace("_", "-")
                            # Convert IES to YS (e.g., ENTITIES → ENTITYS)
                            legacy_tag = f"{xml_tag[:-3]}YS"
                            attribute_types[attr_name]["decorator_name"] = "xml_element_name"
                            attribute_types[attr_name]["decorator_params"] = legacy_tag
                break

    # Add ARRef import if any attribute has is_ref=True
    if attribute_types and any(
        attr_info.get("is_ref", False) for attr_info in attribute_types.values()
    ):
        code += "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef\n"

    # Add type imports if needed
    # Initialize circular and non-circular import sets outside attribute_types block
    circular_imports = set()
    non_circular_imports = set()

    if attribute_types:
        type_imports = set()
        primitive_imports = {}  # Changed from set to dict to track package path
        enum_imports = set()

        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            # Import class types and primitive types
            if is_primitive_type(attr_type, package_data):
                # Find the package path for this primitive
                for package_path, data in package_data.items():
                    if "primitives" in data:
                        for prim in data["primitives"]:
                            if prim["name"] == attr_type:
                                primitive_imports[attr_type] = package_path
                                break
                    if attr_type in primitive_imports:
                        break
            elif is_enum_type(attr_type, package_data):
                enum_imports.add(attr_type)
            elif not attr_type.startswith("any ("):
                # Import class types (skip polymorphic "any (xxx)" types)
                type_imports.add(attr_type)

        # Add import statements for enum types
        if enum_imports:
            # Find package path for each enum
            enums_by_package: Dict[str, List[str]] = {}
            for enum_name in enum_imports:
                for package_path, data in package_data.items():
                    if "enumerations" in data:
                        for enum in data["enumerations"]:
                            if enum["name"] == enum_name:
                                enums_by_package[package_path] = enums_by_package.get(
                                    package_path, []
                                )
                                enums_by_package[package_path].append(enum_name)
                                break
                    if enum_name in [e for pkg in enums_by_package.values() for e in pkg]:
                        break

            for pkg_path, enum_names in sorted(enums_by_package.items()):
                python_path = pkg_path.replace("::", ".")
                code += f"from armodel.models.{python_path} import (\n"
                for i, enum in enumerate(sorted(enum_names)):
                    if i == len(enum_names) - 1:
                        code += f"    {enum},\n"
                    else:
                        code += f"    {enum},\n"
                code += ")\n"

        # Add import statements for primitive types
        # Group primitives by package path
        primitives_by_package: Dict[str, List[str]] = {}
        for prim_name, pkg_path in primitive_imports.items():
            if pkg_path not in primitives_by_package:
                primitives_by_package[pkg_path] = []
            primitives_by_package[pkg_path].append(prim_name)

        for pkg_path, prim_names in sorted(primitives_by_package.items()):
            python_path = pkg_path.replace("::", ".")
            code += f"from armodel.models.{python_path} import (\n"
            for i, prim in enumerate(sorted(prim_names)):
                if i == len(prim_names) - 1:
                    code += f"    {prim},\n"
                else:
                    code += f"    {prim},\n"
            code += ")\n"

        # Add import statements for class types
        # Track already-added imports to prevent duplicates
        # Get parent class import path to avoid importing it again as an attribute type
        added_imports = set()
        if parent_class and parent_class != "ARObject":
            parent_import_path = get_type_import_path(parent_class, package_data)
            if parent_import_path:
                added_imports.add(parent_import_path)

        # Add class_name to prevent self-import (class importing itself)
        # This prevents ARObject from importing itself
        class_import_path = get_type_import_path(class_name, package_data)
        if class_import_path:
            added_imports.add(class_import_path)

        # Get forced TYPE_CHECKING imports for this class
        forced_type_checking_for_class = force_type_checking_imports.get(class_name, [])

        if type_imports:
            for import_type in sorted(type_imports):
                # Skip self-import (class importing itself)
                if import_type == class_name:
                    continue
                import_path = get_type_import_path(import_type, package_data)
                if import_path and import_path not in added_imports:
                    # Check if this import should be forced into TYPE_CHECKING
                    # 1. Check if the import_type is globally forced ("*")
                    forced_globally = force_type_checking_imports.get(import_type) == "*"
                    # 2. Check if this class has specific types forced
                    forced_for_this_class = import_type in forced_type_checking_for_class
                    # 3. Check for circular import via dependency graph
                    is_circular = detect_circular_import(
                        class_name, import_type, package_data, dependency_graph
                    )

                    if forced_globally or forced_for_this_class or is_circular:
                        circular_imports.add((import_type, import_path))
                    else:
                        non_circular_imports.add((import_type, import_path))
                    added_imports.add(import_path)

        # Add non-circular imports directly
        if non_circular_imports:
            for import_type, import_path in sorted(non_circular_imports):
                code += f"{import_path}\n"

        # Add circular imports in TYPE_CHECKING block
        if circular_imports:
            code += "\nif TYPE_CHECKING:\n"
            for import_type, import_path in sorted(circular_imports):
                # Reconstruct just the type name for TYPE_CHECKING import
                # Remove the "from ... import (\n    TYPE,\n)" wrapper
                # and use a simpler TYPE_CHECKING format
                type_package = get_type_package_path(import_type, package_data)
                if type_package:
                    python_path = type_package.replace("::", ".")
                    module_path = f"armodel.models.{python_path}.{to_snake_case(import_type)}"
                    code += f"    from {module_path} import (\n        {import_type},\n    )\n"
            # Add TWO blank lines after TYPE_CHECKING block to ensure two blank lines before class
            # THREE newline characters create TWO blank lines
            code += "\n\n\n"

    # Add abc import for abstract classes BEFORE adding builder imports
    # This ensures builder import deduplication can detect it
    if is_abstract:
        code += "from abc import ABC, abstractmethod\n"

    # Add ARObject import for all classes that use it in the deserialize method
    # The generated deserialize method uses SerializationHelper.find_child_element and SerializationHelper.find_all_child_elements
    # Only add if not already added earlier (after parent class import)
    if class_name != "ARObject":
        ar_object_import = "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject\n"
        if ar_object_import not in code:
            code += ar_object_import
        # Add SerializationHelper import for all classes that use it in serialize/deserialize methods
        # Only add if not already added earlier
        serialization_helper_import = "from armodel.serialization import SerializationHelper\n"
        if serialization_helper_import not in code:
            code += serialization_helper_import

    # Add Builder imports at the top (after all other imports to avoid E402 errors)
    # Deduplicate imports to avoid F811 redefinition errors
    if builder_imports:
        # Split builder imports into lines and check each one
        for builder_import_line in builder_imports.strip().split("\n"):
            # Skip empty lines
            if not builder_import_line.strip():
                continue

            # Check if the exact import line already exists
            if builder_import_line in code:
                continue

            # For 'from X import Y' statements, check for partial duplicates
            # Example: "from abc import ABC, abstractmethod" when "from abc import ABC" exists
            if " import " in builder_import_line:
                import_parts = builder_import_line.split(" import ")
                if len(import_parts) == 2:
                    source = import_parts[0].replace("from ", "").strip()
                    items = [item.strip() for item in import_parts[1].split(",")]

                    # Check if items are already imported from this source
                    # We need to find existing imports from the same source
                    existing_import_pattern = f"from {source} import "
                    if existing_import_pattern in code:
                        # Extract all items already imported from this source
                        import_start = code.find(existing_import_pattern)
                        import_end = code.find("\n", import_start)
                        existing_import = code[import_start:import_end]

                        # Parse existing import to get already imported items
                        existing_items_str = existing_import.split(" import ")[1].strip()
                        existing_items = [item.strip() for item in existing_items_str.split(",")]

                        # Find which items are not yet imported
                        new_items = [item for item in items if item not in existing_items]

                        if new_items:
                            # Add only the new items
                            code += f"from {source} import {', '.join(new_items)}\n"
                        # If all items already exist, skip this import
                        continue

            # Not a duplicate, add the full import line
            code += builder_import_line + "\n"

    # Generate class definition with ABC for abstract classes
    if is_abstract:
        # Abstract classes inherit from ABC
        # (ABC import was already added above)
        if parent_class:
            code += f'''\n
class {class_name}({parent_class}, ABC):
    """AUTOSAR {class_name}."""\n'''
        else:
            code += f'''\n
class {class_name}(ABC):
    """AUTOSAR {class_name}."""\n'''
        # Add is_abstract property for abstract classes
        code += '''
    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

'''
    else:
        # Non-abstract classes
        # Add two blank lines before class definition if NO circular imports
        # If there ARE circular imports, blank lines are already added after TYPE_CHECKING block
        if not circular_imports:
            code += "\n\n"

        # Add @atp_variant decorator if this class uses atpVariation pattern
        atp_type = type_def.get("atp_type", None)
        if atp_type == "atpVariation":
            code += """@atp_variant()

"""

        if parent_class:
            code += f'class {class_name}({parent_class}):\n    """AUTOSAR {class_name}."""\n'
        else:
            code += f'class {class_name}:\n    """AUTOSAR {class_name}."""\n'
        # Add is_abstract property for non-abstract classes
        code += '''
    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

'''

    if is_splitable:
        code += f'''    is_splitable = True
    split_file_name = "{split_file_name}"

'''

    # Add class-level type annotations for get_type_hints() to work
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Determine Python type
            python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)

            # Get Python identifier with Ref suffix if needed
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # For xml_attribute, lang_prefix, language_abbr, xml_element_name, ref_conditional, and instance_ref, use private field with property
            if (
                kind == "xml_attribute"
                or decorator_name == "xml_attribute"
                or decorator_name == "lang_prefix"
                or kind == "language_abbr"
                or decorator_name == "xml_element_name"
                or decorator_name == "ref_conditional"
                or decorator_name == "instance_ref"
            ):
                private_name = f"_{python_name}"
                code += f"    {private_name}: {python_type}\n"
            else:
                # Add class-level annotation
                code += f"    {python_name}: {python_type}\n"

    code += f'''    def __init__(self) -> None:
        """Initialize {class_name}."""\n'''

    # Add super().__init__() call for all classes except ARObject
    if class_name != "ARObject":
        code += """        super().__init__()
"""

    # Add member attributes if requested
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Determine Python type
            python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)

            # Determine initial value based on type
            # Optional types initialize with None
            # list types initialize with []
            # Non-optional types initialize with None
            if python_type.startswith("Optional["):
                initial_value = "None"
            elif python_type.startswith("list["):
                initial_value = "[]"
            else:
                initial_value = "None"

            # Get Python identifier with Ref suffix if needed
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # For xml_attribute, lang_prefix, lang_abbr, xml_element_name, ref_conditional, and instance_ref, use private field
            if (
                kind == "xml_attribute"
                or decorator_name == "xml_attribute"
                or decorator_name == "lang_prefix"
                or decorator_name == "lang_abbr"
                or decorator_name == "xml_element_name"
                or decorator_name == "ref_conditional"
                or decorator_name == "instance_ref"
            ):
                private_name = f"_{python_name}"
                attr_code = f"        self.{private_name}: {python_type} = {initial_value}\n"
                code += attr_code
            else:
                attr_code = f"        self.{python_name}: {python_type} = {initial_value}\n"
                code += attr_code

    # Add property decorators for xml_attribute and l_prefix attributes
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")
            decorator_name = attr_info.get("decorator_name")

            if kind == "xml_attribute":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                # Add @xml_attribute decorator import comment
                # Generate property with xml_attribute decorator
                code += f'''    @property
    @xml_attribute
    def {python_name}(self) -> {attr_type}:
        """Get {python_name} XML attribute."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {attr_type}) -> None:
        """Set {python_name} XML attribute."""
        self.{private_name} = value

'''
            elif decorator_name == "lang_abbr":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                # Extract the XML attribute name from decorator_params
                xml_attr_name = attr_info.get("decorator_params", attr_name.upper())
                # Generate property with lang_abbr decorator
                code += f'''    @property
    @lang_abbr("{xml_attr_name}")
    def {python_name}(self) -> {attr_type}:
        """Get {python_name} language abbreviation attribute."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {attr_type}) -> None:
        """Set {python_name} language abbreviation attribute."""
        self.{private_name} = value

'''
            elif decorator_name == "xml_attribute":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                params = attr_info.get("decorator_params", "")
                # Generate property with xml_attribute decorator
                if params:
                    code += f'''    @property
    @xml_attribute("{params}")
    def {python_name}(self) -> {attr_type}:
        """Get {python_name} XML attribute."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {attr_type}) -> None:
        """Set {python_name} XML attribute."""
        self.{private_name} = value

'''
                else:
                    code += f'''    @property
    @xml_attribute
    def {python_name}(self) -> {attr_type}:
        """Get {python_name} XML attribute."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {attr_type}) -> None:
        """Set {python_name} XML attribute."""
        self.{private_name} = value

'''
            elif decorator_name == "xml_element_name":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                params = attr_info.get("decorator_params", "")
                # Determine Python type for this attribute
                python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)
                # Generate property with xml_element_name decorator
                code += f'''    @property
    @xml_element_name("{params}")
    def {python_name}(self) -> {python_type}:
        """Get {python_name} with custom XML element name."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {python_type}) -> None:
        """Set {python_name} with custom XML element name."""
        self.{private_name} = value

'''
            elif decorator_name == "ref_conditional":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                params = attr_info.get("decorator_params", "")
                # Determine Python type for this attribute
                python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)
                # Generate property with ref_conditional decorator
                code += f'''    @property
    @ref_conditional("{params}")
    def {python_name}(self) -> {python_type}:
        """Get {python_name} with ref_conditional wrapper."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {python_type}) -> None:
        """Set {python_name} with ref_conditional wrapper."""
        self.{private_name} = value

'''
            elif decorator_name == "instance_ref":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                params = attr_info.get("decorator_params", "")
                # Determine Python type for this attribute
                python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)
                # Extract flatten parameter from decorator_params
                flatten_param = "flatten=True" if "flatten=True" in params else "flatten=False"
                # Generate property with instance_ref decorator
                code += f'''    @property
    @instance_ref({flatten_param})
    def {python_name}(self) -> {python_type}:
        """Get {python_name} instance reference."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {python_type}) -> None:
        """Set {python_name} instance reference."""
        self.{private_name} = value

'''
            elif decorator_name == "lang_prefix":
                python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
                private_name = f"_{python_name}"
                # Determine Python type for this attribute
                python_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)
                # Extract the tag from decorator_params (e.g., "L-1", "L-10", "L-GRAPHIC")
                lang_prefix_tag = attr_info.get("decorator_params", "")
                # Generate property with lang_prefix decorator
                code += f'''    @property
    @lang_prefix("{lang_prefix_tag}")
    def {python_name}(self) -> {python_type}:
        """Get {python_name} with language-specific wrapper."""
        return self.{private_name}

    @{python_name}.setter
    def {python_name}(self, value: {python_type}) -> None:
        """Set {python_name} with language-specific wrapper."""
        self.{private_name} = value

'''

    # Add blank line between __init__ and serialize/deserialize methods
    code += "\n"

    # Add serialize/deserialize methods
    # Special handling for ARObject which implements the reflection-based pattern
    # All other classes get optimized serialize() and deserialize() methods
    if class_name == "ARObject":
        # ARObject uses reflection-based serialization framework
        # Add serialize(), deserialize(), and helper methods
        code += _generate_ar_object_methods()
    elif type_def.get("atp_type") == "atpVariation":
        # atpVariant classes use custom serialize/deserialize methods
        # that wrap attributes in VARIANTS/CONDITIONAL structure
        serialize_code = _generate_serialize_method_for_atp_variant(
            class_name, attribute_types, parent_class, package_data
        )
        deserialize_code = _generate_deserialize_method_for_atp_variant(
            class_name, attribute_types, parent_class, package_data
        )
        code += serialize_code + deserialize_code
    elif attribute_types and any(
        attr_info.get("decorator_name") == "lang_prefix" for attr_info in attribute_types.values()
    ):
        # Classes with lang_prefix attributes need custom serialize/deserialize methods
        # because they use lang_prefix decorator handling
        if parent_class and parent_class != "ARObject":
            # Parent class doesn't use reflection, so we need custom methods
            serialize_code = _generate_serialize_method(
                class_name, attribute_types, parent_class, package_data
            )
            deserialize_code = _generate_deserialize_method(
                class_name, attribute_types, parent_class, package_data
            )
            code += serialize_code + deserialize_code
        else:
            # Parent is ARObject, still need to generate custom methods
            # because ARObject.serialize() only handles checksum and timestamp
            serialize_code = _generate_serialize_method(
                class_name, attribute_types, parent_class, package_data
            )
            deserialize_code = _generate_deserialize_method(
                class_name, attribute_types, parent_class, package_data
            )
            code += serialize_code + deserialize_code
    else:
        # For other classes, generate optimized serialize() and deserialize() methods
        # These methods parse/serialize XML directly for better performance
        serialize_code = _generate_serialize_method(
            class_name, attribute_types, parent_class, package_data
        )
        deserialize_code = _generate_deserialize_method(
            class_name, attribute_types, parent_class, package_data
        )
        code += serialize_code + deserialize_code

    return code


def _generate_deserialize_method(
    class_name: str,
    attribute_types: Dict[str, Dict[str, Any]],
    parent_class: Optional[str],
    package_data: Dict[str, Dict[str, Any]],
) -> str:
    """Generate optimized deserialize() method for a class.

    Args:
        class_name: Name of the class
        attribute_types: Dictionary of attribute information
        parent_class: Name of parent class (if any)
        package_data: Package data dictionary

    Returns:
        Generated deserialize() method code
    """
    code = f'''    @classmethod
    def deserialize(cls, element: ET.Element) -> "{class_name}":
        """Deserialize XML element to {class_name} object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized {class_name} object
        """
'''

    # If class has no direct attributes but has a parent class,
    # delegate to parent's deserialize method to handle inherited attributes
    if not attribute_types and parent_class:
        code += f"""        # Delegate to parent class to handle inherited attributes
        return super({class_name}, cls).deserialize(element)

"""
        return code

    # If class has a parent class, call parent's deserialize first
    # to handle inherited attributes, then parse own attributes
    if parent_class:
        code += f"""        # First, call parent's deserialize to handle inherited attributes
        obj = super({class_name}, cls).deserialize(element)

"""
    else:
        # No parent class to handle, create instance directly
        code += """        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

"""

    # Generate code to parse each attribute
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Debug output for ReferenceBase package attribute
            if class_name == "ReferenceBase" and attr_name == "package":
                print(
                    f"DEBUG [deserialize]: class={class_name}, attr={attr_name}, is_ref={is_ref}, kind={kind}, is_ref and kind == 'reference'={is_ref and kind == 'reference'}"
                )

            # Get Python identifier
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
            # Convert attribute name to snake_case then to XML tag (UPPER-CASE-WITH-HYPHENS)
            snake_name = to_snake_case(attr_name)
            xml_tag = snake_name.upper().replace("_", "-")
            # Add -TREF or -REF suffix for reference attributes with multiplicity != "*"
            # Container elements (multiplicity "*") should not have -REF suffix
            # Note: iref kind is handled separately below and doesn't get -REF suffix
            if is_ref and multiplicity != "*" and kind != "iref":
                # Use the kind field from JSON to determine the suffix
                # "tref" -> -TREF, "ref" -> -REF
                if kind == "tref":
                    xml_tag = f"{xml_tag}-TREF"
                else:
                    xml_tag = f"{xml_tag}-REF"

            # Convert "any (xxx)" types to "Any" for generation
            effective_type = attr_type
            if attr_type.startswith("any ("):
                effective_type = "Any"

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # Handle xml_attribute - parse from XML attributes, not child elements
            if kind == "xml_attribute" or decorator_name == "xml_attribute":
                # Get decorator params if present for custom XML attribute name
                decorator_params = attr_info.get("decorator_params", None)
                if decorator_params:
                    xml_attr_tag = decorator_params  # Use custom attribute name from decorator
                else:
                    xml_attr_tag = xml_tag  # Use auto-converted name
                attribute_value = f'element.attrib["{xml_attr_tag}"]'
                code += f'''        # Parse {python_name} from XML attribute
        if "{xml_attr_tag}" in element.attrib:
            {_generate_value_extraction_code_for_attribute(effective_type, attribute_value, package_data, python_name, is_ref)}
            obj.{python_name} = {python_name}_value

'''
            elif decorator_name == "lang_abbr":
                # Handle lang_abbr - parse from custom XML attribute name
                xml_attr_name = attr_info.get("decorator_params", attr_name.upper())
                attribute_value = f'element.attrib["{xml_attr_name}"]'
                code += f'''        # Parse {python_name} from language abbreviation XML attribute
        if "{xml_attr_name}" in element.attrib:
            {_generate_value_extraction_code_for_attribute(effective_type, attribute_value, package_data, python_name, is_ref)}
            obj.{python_name} = {python_name}_value

'''
            elif kind == "iref":
                # Handle iref kind - instance reference with special wrapper
                # The outer wrapper is attribute name + -IREF
                # Determine if this should be flattened based on decorator parameter
                decorator_name = attr_info.get("decorator_name")
                decorator_params = attr_info.get("decorator_params")
                
                # Determine if this should be flattened based on decorator parameter
                should_flatten = False
                if decorator_name == "instance_ref" and decorator_params:
                    # Parse decorator params (format: "flatten=True" or "flatten=False")
                    if "flatten=True" in decorator_params:
                        should_flatten = True
                    elif "flatten=False" in decorator_params:
                        should_flatten = False

                iref_wrapper_tag = f"{xml_tag}-IREF"

                if should_flatten:
                    # Flattened type: deserialize wrapper element directly as the type
                    code += f'''        # Parse {python_name} (instance reference from wrapper "{iref_wrapper_tag}")
        wrapper = SerializationHelper.find_child_element(element, "{iref_wrapper_tag}")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            {python_name}_value = SerializationHelper.deserialize_by_tag(wrapper, "{effective_type}")
            obj.{python_name} = {python_name}_value

'''
                else:
                    # Non-flattened type: deserialize from child element
                    code += f'''        # Parse {python_name} (instance reference from wrapper "{iref_wrapper_tag}")
        wrapper = SerializationHelper.find_child_element(element, "{iref_wrapper_tag}")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                {_generate_value_extraction_code(effective_type, "inner_elem", package_data, python_name, is_ref, kind)}
                obj.{python_name} = {python_name}_value

'''
            elif multiplicity == "*":
                # List type
                # Check if the XML tag ends with "S" (plural form like PACKAGES, ELEMENTS)
                # If so, it's a container element and we need to create a wrapper
                if xml_tag.endswith("S"):
                    # Check if ref_conditional decorator is present
                    decorator_name = attr_info.get("decorator_name")
                    if decorator_name == "ref_conditional":
                        # Use ref_conditional pattern: container stays as-is, each item wrapped in -REF-CONDITIONAL
                        container_tag = attr_info.get("decorator_params", xml_tag)
                        singular = container_tag[:-1]  # Remove trailing S
                        conditional_tag = f"{singular}-REF-CONDITIONAL"
                        ref_tag = f"{singular}-REF"
                    elif decorator_name == "xml_element_name":
                        # Parse decorator params: can be single value or multi-level path separated by '/'
                        # Examples: "PROVIDED-ENTRYS" or "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF"
                        decorator_params = attr_info.get("decorator_params", xml_tag)
                        if isinstance(decorator_params, str) and "/" in decorator_params:
                            # Multi-level nesting: split on '/' to get all levels
                            tag_levels = [level.strip() for level in decorator_params.split("/")]
                            container_tag = tag_levels[0]  # Outermost container
                            child_tag = tag_levels[-1]  # Innermost tag for individual items
                            inner_tags = tag_levels[1:-1]  # Intermediate nesting levels (if any)
                        else:
                            # Single parameter: just container tag
                            container_tag = (
                                decorator_params if isinstance(decorator_params, str) else xml_tag
                            )
                            child_tag = None
                            inner_tags = []
                    else:
                        # Container element (e.g., AR-PACKAGES, ELEMENTS, USE-INSTEAD-REFS)
                        # For reference lists (is_ref=True), the container tag should be singular + -REFS
                        # For non-reference lists, the container tag is the plural form (e.g., LIFE-CYCLE-INFOS)
                        container_tag = xml_tag
                        child_tag = None
                        inner_tags = []
                        if is_ref:
                            # For reference lists, the container tag is singular form + -REFS
                            # e.g., USE-INSTEADS -> USE-INSTEAD-REFS
                            singular = xml_tag[:-1]  # Remove trailing 'S'
                            container_tag = f"{singular}-REFS"

                    code += f'''        # Parse {python_name} (list from container "{container_tag}")
        obj.{python_name} = []
        container = SerializationHelper.find_child_element(element, "{container_tag}")'''

                    # Add navigation through nested levels if inner_tags is not empty
                    if inner_tags:
                        code += """        # Navigate through nested container levels"""
                        for inner_tag in inner_tags:
                            code += f'''
        if container is not None:
            container = SerializationHelper.find_child_element(container, "{inner_tag}")'''

                    code += """
        if container is not None:
            for child in container:
"""

                    # For reference lists, check if child is a reference element and use ARRef.deserialize()
                    # For primitive/enum lists, extract text directly
                    # For non-reference class lists, deserialize each child element dynamically based on its tag
                    if is_ref:
                        # Check if ref_conditional decorator is present
                        if decorator_name == "ref_conditional":
                            # Unwrap -REF-CONDITIONAL to extract the inner -REF
                            code += f'''                # Unwrap -REF-CONDITIONAL to extract the inner -REF
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag == "{conditional_tag}":
                    ref_child = SerializationHelper.find_child_element(child, "{ref_tag}")
                    if ref_child is not None:
                        child_value = ARRef.deserialize(ref_child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
'''
                        # Use the child_tag from decorator if specified to match specific child tag
                        elif child_tag:
                            code += f'''                # Check if child matches expected reference tag "{child_tag}"
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag == "{child_tag}":
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
'''
                        else:
                            code += """                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
"""
                    elif is_primitive_type(attr_type, package_data):
                        # Simple primitive type - extract text directly
                        code += f"""                # Extract primitive value ({attr_type}) as text
                child_value = child.text
"""
                    elif is_enum_type(attr_type, package_data):
                        # Enum type - use deserialize method for proper conversion
                        code += f"""                # Extract enum value ({attr_type})
                child_value = {attr_type}.deserialize(child)
"""
                    else:
                        # Complex object type - deserialize dynamically
                        code += """                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
"""

                    code += f"""                if child_value is not None:
                    obj.{python_name}.append(child_value)

"""
                else:
                    # Non-container list type (multiple instances of the same element)
                    # Check if this is a lang_prefix attribute
                    if decorator_name == "lang_prefix":
                        # lang_prefix attributes use the tag from decorator_params (e.g., L-1, L-10)
                        lang_prefix_tag = attr_info.get("decorator_params", "")
                        code += f'''        # Parse {python_name} (list with lang_prefix "{lang_prefix_tag}")
        obj.{python_name} = []
        for child in SerializationHelper.find_all_child_elements(element, "{lang_prefix_tag}"):
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name}.append({python_name}_value)

'''
                    else:
                        # Regular non-container list
                        code += f'''        # Parse {python_name} (list)
        obj.{python_name} = []
        for child in SerializationHelper.find_all_child_elements(element, "{xml_tag}"):
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name}.append({python_name}_value)

'''
            else:
                # Single value type
                code += f'''        # Parse {python_name}
        child = SerializationHelper.find_child_element(element, "{xml_tag}")
        if child is not None:
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name} = {python_name}_value

'''

    code += """        return obj

"""
    return code


def _generate_value_extraction_code(
    attr_type: str,
    element_var: str,
    package_data: Dict[str, Dict[str, Any]],
    var_name: str,
    is_ref: bool = False,
    kind: str = "attribute",
) -> str:
    """Generate code to extract value from XML element.

    Args:
        attr_type: AUTOSAR type name
        element_var: Variable name for the XML element
        package_data: Package data dictionary
        var_name: Variable name to store the result
        is_ref: Whether this is a reference type (should use ARRef.deserialize)
        kind: Kind of attribute (e.g., "attribute", "ref", "tref", "iref")

    Returns:
        Generated code for value extraction
    """
    value_var = f"{var_name}_value"

    # Handle reference types (ARRef)
    # Note: iref kind represents instance references which are complex objects, not simple references
    # For iref kind, deserialize as the actual class type, not as ARRef
    if is_ref and kind != "iref":
        # Use ARRef.deserialize() for reference types
        return f"""{value_var} = ARRef.deserialize({element_var})"""

    # Handle primitive types
    if is_primitive_type(attr_type, package_data):
        # Check if this primitive has attributes (e.g., Limit has interval_type)
        # If it has attributes, we need to deserialize it as an object
        has_attributes = False
        for package_path, data in package_data.items():
            if "primitives" in data:
                for prim in data["primitives"]:
                    if prim["name"] == attr_type:
                        # Check if primitive has attributes
                        if "attributes" in prim and prim["attributes"]:
                            has_attributes = True
                        break
                if has_attributes:
                    break

        if has_attributes:
            # Use deserialize for primitives with attributes
            return f'''{value_var} = SerializationHelper.deserialize_by_tag({element_var}, "{attr_type}")'''
        else:
            # Simple primitive - just get text
            return f"""{value_var} = {element_var}.text"""

    # Handle enum types
    elif is_enum_type(attr_type, package_data):
        # Use the enum's deserialize method for proper case-insensitive conversion
        return f"""{value_var} = {attr_type}.deserialize({element_var})"""

    # Handle Any type (polymorphic)
    elif attr_type == "Any":
        return f"""{value_var} = {element_var}.text"""

    # Handle class types
    else:
        # Check if the type has l_prefix attributes
        # If so, use _deserialize_with_type instead of _deserialize_by_tag
        # because the XML tag is a wrapper (like USED-LANGUAGES) not a class name
        has_lang_prefix = False
        for package_path, data in package_data.items():
            if "classes" in data:
                for cls in data["classes"]:
                    if cls["name"] == attr_type:
                        # Check if any attribute has decorator_name == "lang_prefix"
                        if "attributes" in cls:
                            for attr_info in cls["attributes"].values():
                                if attr_info.get("decorator_name") == "lang_prefix":
                                    has_lang_prefix = True
                                    break
                        break
                if has_lang_prefix:
                    break

        if has_lang_prefix:
            # Use _deserialize_with_type for types with lang_prefix attributes
            # This deserializes the element directly as the specified type
            return f'''{value_var} = SerializationHelper.deserialize_with_type({element_var}, "{attr_type}")'''
        elif kind == "iref":
            # For iref kind, don't pass class_name
            # This allows deserializing based on the actual XML tag (concrete subclass)
            # instead of forcing the abstract base class type
            return f"""{value_var} = SerializationHelper.deserialize_by_tag({element_var})"""
        else:
            # Use SerializationHelper.deserialize_by_tag to avoid TYPE_CHECKING issues
            # This doesn't require the type to be imported at runtime
            return f'''{value_var} = SerializationHelper.deserialize_by_tag({element_var}, "{attr_type}")'''


def _generate_value_extraction_code_for_attribute(
    attr_type: str,
    attribute_value: str,
    package_data: Dict[str, Dict[str, Any]],
    var_name: str,
    is_ref: bool = False,
) -> str:
    """Generate code to extract value from XML attribute.

    Args:
        attr_type: AUTOSAR type name
        attribute_value: String containing the XML attribute value (e.g., "element.attrib['TAG']")
        package_data: Package data dictionary
        var_name: Variable name to store the result
        is_ref: Whether this is a reference type (should use ARRef.deserialize)

    Returns:
        Generated code for value extraction
    """
    value_var = f"{var_name}_value"

    # Handle reference types (ARRef)
    if is_ref:
        # Use ARRef.deserialize() for reference types - need to create a fake element
        return f"""from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
        fake_elem = ET.Element("FAKE")
        fake_elem.text = {attribute_value}
        {value_var} = ARRef.deserialize(fake_elem)"""

    # Handle primitive types
    if is_primitive_type(attr_type, package_data):
        # Check if this primitive has attributes (e.g., Limit has interval_type)
        # If it has attributes, we need to deserialize it as an object
        has_attributes = False
        for package_path, data in package_data.items():
            if "primitives" in data:
                for prim in data["primitives"]:
                    if prim["name"] == attr_type:
                        # Check if primitive has attributes
                        if "attributes" in prim and prim["attributes"]:
                            has_attributes = True
                        break
                if has_attributes:
                    break

        if has_attributes:
            # Use deserialize for primitives with attributes - need to create a fake element
            return f'''fake_elem = ET.Element("FAKE")
            fake_elem.text = {attribute_value}
            {value_var} = SerializationHelper.deserialize_by_tag(fake_elem, "{attr_type}")'''
        else:
            # Simple primitive - just use the string value directly
            return f"""{value_var} = {attribute_value}"""

    # Handle enum types
    elif is_enum_type(attr_type, package_data):
        # Create enum value from string
        return f"""{value_var} = {attr_type}({attribute_value})"""

    # Handle Any type (polymorphic)
    elif attr_type == "Any":
        return f"""{value_var} = {attribute_value}"""

    # Handle class types (should not happen for XML attributes)
    else:
        # Just use the string value
        return f"""{value_var} = {attribute_value}"""


def _generate_ar_object_methods() -> str:
    """Generate the serialize/deserialize methods for ARObject.

    Returns:
        Generated code for ARObject methods
    """
    return r'''
    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize object to XML element using reflection.

        Automatically discovers all non-private attributes via vars(self),
        converts names to XML tags, and serializes them as child elements.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
# Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)
            # Skip private attributes
            if name.startswith('_'):
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(name)

            # Skip None values
            if value is None:
                continue

            # Check if this should be an XML attribute (via decorator)
            if self._is_xml_attribute(name):
                elem.set(xml_tag, str(value))
            elif hasattr(value, 'serialize'):
                # Recursively serialize child objects
                child = value.serialize(namespace)
                elem.append(child)
            elif isinstance(value, list):
                # Serialize list items - create wrapper element
                wrapper = ET.Element(xml_tag)
                for item in value:
                    if hasattr(item, 'serialize'):
                        wrapper.append(item.serialize(namespace))
                    else:
                        child = ET.Element(xml_tag)
                        child.text = str(item)
                        wrapper.append(child)
                elem.append(wrapper)
            else:
                # Primitive value - create element with text content
                child = ET.Element(xml_tag)
                child.text = str(value)
                elem.append(child)

        return elem

    def _get_xml_tag(self) -> str:
        """Get XML tag name for this class.

        Auto-generates from class name using NameConverter.

        Returns:
            XML tag name
        """
        # Auto-generate from class name
        return NameConverter.to_xml_tag(self.__class__.__name__)

    def _is_xml_attribute(self, attr_name: str) -> bool:
        """Check if an attribute should be serialized as XML attribute.

        Checks for @xml_attribute decorator on the property.

        Args:
            attr_name: Name of the attribute to check

        Returns:
            True if should be XML attribute, False if element
        """
        # Get the property if it exists
        prop = getattr(self.__class__, attr_name, None)
        if prop and hasattr(prop, 'fget'):
            # Check if the property getter has the decorator marker
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

        # Check if the attribute itself has the marker
        attr = getattr(self.__class__, attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute

        return False

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARObject":
        """Deserialize XML element to Python object.

        Creates a new instance and populates attributes by matching
        XML tags to Python attribute names.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Python object
        """
        # Create instance without calling __init__
        obj = cls.__new__(cls)

        # Call __init__ to set default values
        obj.__init__()

        # Get type hints to know what attributes to expect
        try:
            type_hints = get_type_hints(cls)
        except Exception:
            # Fallback: Use __annotations__ directly if get_type_hints fails
            # This can happen due to circular imports or missing types
            # Note: Annotations will be strings due to 'from __future__ import annotations'
            type_hints = {}
            # Collect annotations from entire MRO
            for base_cls in cls.__mro__:
                if hasattr(base_cls, '__annotations__'):
                    for attr_name, attr_type_str in base_cls.__annotations__.items():
                        if attr_name not in type_hints:
                            # Keep as string - _extract_value will handle it
                            type_hints[attr_name] = attr_type_str

        # Helper function to strip namespace from tag
        def strip_namespace(tag: str) -> str:
            """Strip namespace from XML tag.

            Args:
                tag: XML tag with optional namespace

            Returns:
                Tag without namespace
            """
            if '}' in tag:
                return tag.split('}')[1]
            return tag

        # Strip namespace from element tag for matching
        element_tag_stripped = strip_namespace(element.tag)

        # Process each attribute from type hints
        for attr_name, attr_type in type_hints.items():
            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(attr_name)

            # Check if this should be an XML attribute
            if SerializationHelper.is_xml_attribute_static(cls, attr_name):
                value = element.get(xml_tag)
            else:
                # Find child element - try both with and without namespace
                child = element.find(xml_tag)
                if child is None:
                    # Try to find by matching stripped tag names
                    for elem in element:
                        if strip_namespace(elem.tag) == xml_tag:
                            child = elem
                            break

                if child is not None:
                    # Get value based on type
                    value = SerializationHelper.extract_value(child, attr_type)
                else:
                    value = None

            # Set attribute
            setattr(obj, attr_name, value)

        return obj

    @staticmethod
    def _is_xml_attribute_static(cls, attr_name: str) -> bool:
        """Static version to check if attribute should be XML attribute.

        Args:
            cls: The class to check
            attr_name: Name of the attribute

        Returns:
            True if should be XML attribute
        """
        prop = getattr(cls, attr_name, None)
        if prop and hasattr(prop, 'fget'):
            return hasattr(prop.fget, '_is_xml_attribute') and prop.fget._is_xml_attribute

        attr = getattr(cls, attr_name, None)
        if attr and hasattr(attr, '_is_xml_attribute'):
            return attr._is_xml_attribute

        return False

    @staticmethod
    def _import_class_by_name(class_name: str):
        """Import a class by name from armodel.models.M2.

        Args:
            class_name: Name of the class to import (e.g., "ARPackage")

        Returns:
            The imported class, or None if not found
        """
        import sys
        import importlib

        # Check if already in sys.modules
        for module_name, module in sys.modules.items():
            if module_name.startswith('armodel.models.M2'):
                if hasattr(module, class_name):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):
                        return cls

        # Try to import from known locations
        # Convert class name to snake_case for filename
        class_filename = class_name.replace('<', '_').replace('>', '_')

        # Common package paths to search
        search_paths = [
            f'armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.{class_name}.{class_filename}',
            f'armodel.models.M2.AUTOSARTemplates.{class_name}.{class_filename}',
            f'armodel.models.M2.MSR.{class_name}.{class_filename}',
        ]

        for module_path in search_paths:
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, class_name):
                    return getattr(module, class_name)
            except (ImportError, ModuleNotFoundError):
                continue

        # Fallback: try searching through all M2 modules
        try:
            from armodel.models.M2 import AUTOSARTemplates, MSR

            # Search in AUTOSARTemplates
            if hasattr(AUTOSARTemplates, '__path__'):
                from pkgutil import walk_packages
                for importer, modname, ispkg in walk_packages(AUTOSARTemplates.__path__, AUTOSARTemplates.__name__ + '.'):
                    try:
                        module = importlib.import_module(modname)
                        if hasattr(module, class_name):
                            cls = getattr(module, class_name)
                            if isinstance(cls, type):
                                return cls
                    except (ImportError, ModuleNotFoundError):
                        continue
        except Exception:
            pass

        return None

    @staticmethod
    def _extract_value(element: ET.Element, attr_type):
        """Extract value from XML element based on type.

        Args:
            element: XML element
            attr_type: Expected type (from type hints) - can be type object or string

        Returns:
            Extracted value
        """
        if element is None:
            return None

        # Handle string type annotations (from __annotations__ with future import)
        if isinstance(attr_type, str):
            # Parse string type annotations like "list[ARPackage]" or "Optional[SomeType]"
            import re

            # Extract list type
            list_match = re.match(r'list\[(.+?)\]', attr_type)
            if list_match:
                inner_type_str = list_match.group(1)
                # Find all direct child elements
                children = list(element)

                # Try to import the class and deserialize
                result = []
                for child in children:
                    # Try to deserialize using the class
                    item_class = SerializationHelper.import_class_by_name(inner_type_str)
                    if item_class and hasattr(item_class, 'deserialize'):
                        item = item_class.deserialize(child)
                        result.append(item)
                    else:
                        # Fallback to text content
                        result.append(child.text if child.text else None)

                return result

            # Handle optional types
            optional_match = re.match(r'Optional\[(.+?)\]', attr_type)
            if optional_match:
                inner_type_str = optional_match.group(1)
                # Try to import and deserialize
                item_class = SerializationHelper.import_class_by_name(inner_type_str)
                if item_class and hasattr(item_class, 'deserialize'):
                    return item_class.deserialize(element)

                # Fallback to text content
                return element.text if element.text else None

            # For simple class names, try to import and deserialize
            item_class = SerializationHelper.import_class_by_name(attr_type)
            if item_class and hasattr(item_class, 'deserialize'):
                return item_class.deserialize(element)

            # For simple string types, just return text
            return element.text if element.text else None

        # Check if it's a list type
        if get_origin(attr_type) is list:
            # Get the element type
            type_args = get_args(attr_type)
            if type_args:
                item_type = type_args[0]

                # Find all direct child elements (not grandchildren)
                children = list(element)

                # Deserialize each child element
                result = []
                for child in children:
                    # For object types, deserialize recursively
                    if hasattr(item_type, 'deserialize'):
                        item = item_type.deserialize(child)
                        result.append(item)
                    else:
                        # For primitives, get text content
                        result.append(child.text if child.text else None)

                return result

        # Check if it's an Optional type
        if get_origin(attr_type) is Union:
            type_args = get_args(attr_type)
            # Get the first non-None type
            for arg in type_args:
                if arg is not type(None):
                    attr_type = arg
                    break

        # For object types with deserialize method, recursively deserialize
        # Check if attr_type is a class (not a primitive type like str, int, etc.)
        if isinstance(attr_type, type) and hasattr(attr_type, 'deserialize'):
            return attr_type.deserialize(element)

        # For primitive types, return text content
        text = element.text
        if text is None:
            return None

        # Simple type conversions for primitives
        if attr_type == str:
            return text
        elif attr_type == int:
            try:
                return int(text)
            except ValueError:
                return text
        elif attr_type == float:
            try:
                return float(text)
            except ValueError:
                return text
        elif attr_type == bool:
            return text.lower() in ('true', '1', 'yes')
        else:
            # Default to string
            return text
'''


def _collect_all_attributes(
    class_name: str,
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    package_path: str,
) -> List[Dict[str, Any]]:
    """Recursively collect all attributes from inheritance chain.

    Args:
        class_name: Name of the class to collect attributes for
        hierarchy_info: Class hierarchy information
        package_data: Package data containing class definitions
        package_path: Path to the package (not used, searches all packages)

    Returns:
        List of all attributes (child first, then parents)
    """
    all_attributes = []

    # Get parent class from hierarchy
    parent_class = None
    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name].get("parent")

    # Recursively collect parent attributes first
    if parent_class and parent_class != "ARObject":
        parent_attrs = _collect_all_attributes(
            parent_class, hierarchy_info, package_data, package_path
        )
        all_attributes.extend(parent_attrs)

    # Search for current class in all packages
    class_data = None
    for pkg_path, pkg_data in package_data.items():
        if "classes" in pkg_data:
            for cls in pkg_data["classes"]:
                if cls["name"] == class_name:
                    class_data = cls
                    break
        if class_data:
            break

    # Add current class attributes
    if class_data and "attributes" in class_data:
        attrs = extract_attribute_metadata(class_name, class_data["attributes"])
        all_attributes.extend(attrs)

    return all_attributes


def _collect_current_class_attributes(
    class_name: str,
    package_data: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Collect only the current class's own attributes (not inherited).

    Args:
        class_name: Name of the class to collect attributes for
        package_data: Package data containing class definitions

    Returns:
        List of current class's own attributes
    """
    # Search for current class in all packages
    class_data = None
    for pkg_path, pkg_data in package_data.items():
        if "classes" in pkg_data:
            for cls in pkg_data["classes"]:
                if cls["name"] == class_name:
                    class_data = cls
                    break
        if class_data:
            break

    # Add current class attributes only
    if class_data and "attributes" in class_data:
        return extract_attribute_metadata(class_name, class_data["attributes"])

    return []


def _get_builder_parent_class(
    class_name: str,
    hierarchy_info: Dict[str, Dict[str, Any]],
) -> Optional[str]:
    """Get the parent Builder class name.

    Args:
        class_name: Name of the class
        hierarchy_info: Class hierarchy information

    Returns:
        Parent Builder class name or None
    """
    # Get parent class from hierarchy
    parent_class = None
    if class_name in hierarchy_info:
        parent_class = hierarchy_info[class_name].get("parent")

    # If parent is ARObject, no Builder inheritance needed
    if not parent_class or parent_class == "ARObject":
        return None

    # Return parent Builder class name (allow abstract parents for method reuse)
    return f"{parent_class}Builder"


def _generate_with_method(
    class_name: str,
    attr_name: str,
    attr_type: str,
    is_optional: bool,
) -> str:
    """Generate a with_* method for a single attribute.

    Args:
        class_name: Name of the class
        attr_name: Name of the attribute (camelCase from JSON)
        attr_type: Type of the attribute
        is_optional: Whether the attribute is optional

    Returns:
        Generated with_* method code
    """
    # Convert attribute name to snake_case for method name
    snake_attr_name = to_snake_case(attr_name)
    method_name = f"with_{snake_attr_name}"
    param_type = f"Optional[{attr_type}]" if is_optional else attr_type

    # Check if type coercion should be applied
    base_type = extract_base_type(attr_type)
    coerce_func = get_type_coercion_function(base_type)

    # Build the assignment line - use setattr for Python keywords
    python_keywords = {
        "class",
        "def",
        "return",
        "if",
        "else",
        "elif",
        "for",
        "while",
        "import",
        "from",
        "try",
        "except",
        "finally",
        "with",
        "lambda",
        "raise",
        "pass",
        "break",
        "continue",
        "and",
        "or",
        "not",
        "in",
        "is",
        "assert",
        "async",
        "await",
        "global",
        "nonlocal",
        "yield",
    }

    if snake_attr_name in python_keywords:
        # Use setattr for Python keywords
        if coerce_func and should_apply_type_coercion(base_type):
            assignment = f"setattr(self._obj, '{snake_attr_name}', self._{coerce_func}(value))"
        else:
            assignment = f"setattr(self._obj, '{snake_attr_name}', value)"
    else:
        # Direct assignment for non-keywords
        if coerce_func and should_apply_type_coercion(base_type):
            assignment = f"self._obj.{snake_attr_name} = self._{coerce_func}(value)"
        else:
            assignment = f"self._obj.{snake_attr_name} = value"

    # Generate the method
    code = f'''
    def {method_name}(self, value: {param_type}) -> "{class_name}Builder":
        """Set {snake_attr_name} attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not {is_optional}:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        {assignment}
        return self
'''

    return code


def _generate_with_items_method(
    class_name: str,
    attr_name: str,
    item_type: str,
) -> str:
    """Generate with_items method for list attributes.

    Args:
        class_name: Name of the class
        attr_name: Name of the list attribute (camelCase from JSON)
        item_type: Type of items in the list

    Returns:
        Generated with_items method code
    """
    # Convert attribute name to snake_case
    snake_attr_name = to_snake_case(attr_name)
    method_name = f"with_{snake_attr_name}"

    # Check if attribute name is a Python keyword
    python_keywords = {
        "class",
        "def",
        "return",
        "if",
        "else",
        "elif",
        "for",
        "while",
        "import",
        "from",
        "try",
        "except",
        "finally",
        "with",
        "lambda",
        "raise",
        "pass",
        "break",
        "continue",
        "and",
        "or",
        "not",
        "in",
        "is",
        "assert",
        "async",
        "await",
        "global",
        "nonlocal",
        "yield",
    }

    if snake_attr_name in python_keywords:
        assignment = f"setattr(self._obj, '{snake_attr_name}', list(items) if items else [])"
    else:
        assignment = f"self._obj.{snake_attr_name} = list(items) if items else []"

    code = f'''
    def {method_name}(self, items: list[{item_type}]) -> "{class_name}Builder":
        """Set {snake_attr_name} list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        {assignment}
        return self
'''

    return code


def _generate_list_methods(
    class_name: str,
    attr_name: str,
    item_type: str,
) -> List[str]:
    """Generate add_item and clear_items methods for list attributes.

    Args:
        class_name: Name of the class
        attr_name: Name of the list attribute (camelCase from JSON)
        item_type: Type of items in the list

    Returns:
        List of generated method code
    """
    # Convert attribute name to snake_case
    snake_attr_name = to_snake_case(attr_name)

    # Generate singular name for add_* method
    singular_name = (
        snake_attr_name.rstrip("s") if snake_attr_name.endswith("s") else snake_attr_name[:-1]
    )

    # Check if attribute name is a Python keyword
    python_keywords = {
        "class",
        "def",
        "return",
        "if",
        "else",
        "elif",
        "for",
        "while",
        "import",
        "from",
        "try",
        "except",
        "finally",
        "with",
        "lambda",
        "raise",
        "pass",
        "break",
        "continue",
        "and",
        "or",
        "not",
        "in",
        "is",
        "assert",
        "async",
        "await",
        "global",
        "nonlocal",
        "yield",
    }

    if snake_attr_name in python_keywords:
        append_line = f"getattr(self._obj, '{snake_attr_name}').append(item)"  # noqa: F841
        clear_line = f"setattr(self._obj, '{snake_attr_name}', [])"  # noqa: F841
    else:
        append_line = f"self._obj.{snake_attr_name}.append(item)"  # noqa: F841
        clear_line = f"self._obj.{snake_attr_name} = []"  # noqa: F841

    # Add method
    add_method = (
        f'''
    def add_{singular_name}(self, item: {item_type}) -> "{class_name}Builder":
        """Add a single item to '''
        + snake_attr_name
        + ''' list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        '''
        + append_line
        + """
        return self
"""
    )

    # Clear method
    clear_method = (
        f'''
    def clear_{snake_attr_name}(self) -> "{class_name}Builder":
        """Clear all items from '''
        + snake_attr_name
        + ''' list.

        Returns:
            self for method chaining
        """
        '''
        + clear_line
        + """
        return self
"""
    )

    return [add_method, clear_method]


def _generate_validation_helper() -> str:
    """Generate validation helper method for Builder class.

    Returns:
        Generated validation helper code
    """
    return '''
    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object
'''


def generate_builder_code(
    type_def: Dict[str, Any],
    hierarchy_info: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    include_members: bool = False,
) -> tuple[str, str]:
    """Generate builder class code from type definition.

    Args:
        type_def: Type definition from mapping.json
        hierarchy_info: Class hierarchy information
        package_data: Package data containing class definitions
        include_members: Whether to include member methods

    Returns:
        Tuple of (builder_imports, builder_class_code) where:
        - builder_imports: Import statements needed for the Builder class
        - builder_class_code: The Builder class definition without imports
    """
    class_name = type_def["name"]
    is_abstract = type_def.get("is_abstract", False)

    builder_name = f"{class_name}Builder"

    # Get parent Builder class
    builder_parent = _get_builder_parent_class(class_name, hierarchy_info)

    # Build inheritance list
    # Check if parent Builder (or its ancestors) already inherits from BuilderBase
    # If so, we don't need to add BuilderBase again (avoids MRO conflict)
    parent_inherits_builderbase = False
    if builder_parent:
        # Check if parent class is abstract (abstract parents inherit from BuilderBase, ABC)
        parent_class = builder_parent.replace("Builder", "")
        if parent_class in hierarchy_info and hierarchy_info[parent_class].get(
            "is_abstract", False
        ):
            parent_inherits_builderbase = True
        # Check if parent class itself is abstract in type_def
        elif parent_class in type_def and type_def.get(parent_class, {}).get("is_abstract", False):
            parent_inherits_builderbase = True

    if parent_inherits_builderbase:
        # Parent or ancestor already inherits from BuilderBase, so we just inherit from parent
        inheritance_parts = [builder_parent]
    elif builder_parent:
        # Parent doesn't inherit from BuilderBase, so we add it
        inheritance_parts = ["BuilderBase", builder_parent]
    else:
        # No parent, we inherit from BuilderBase (and ABC if abstract)
        inheritance_parts = ["BuilderBase"]
        if is_abstract:
            inheritance_parts.append("ABC")

    inheritance_str = ", ".join(inheritance_parts)
    class_def = f"class {builder_name}({inheritance_str}):"

    # ARObject is instantiated without parentheses
    if class_name == "ARObject":
        obj_init = f"{class_name}"
    else:
        obj_init = f"{class_name}()"

    # Generate with_* methods only for current class attributes (not inherited)
    with_methods = []
    list_methods = []

    if include_members and "attributes" in type_def:
        # Collect ONLY current class's own attributes
        current_attrs = _collect_current_class_attributes(class_name, package_data)

        for attr in current_attrs:
            attr_name = attr["name"]
            attr_type = attr["type"]
            is_list = attr["is_list"]
            is_optional = attr["is_optional"]

            if is_list:
                # Generate list-specific methods
                item_type = attr["base_type"]
                with_methods.append(_generate_with_items_method(class_name, attr_name, item_type))
                list_methods.extend(_generate_list_methods(class_name, attr_name, item_type))
            else:
                # Generate standard with_* method
                with_methods.append(
                    _generate_with_method(class_name, attr_name, attr_type, is_optional)
                )

    # Import ABC if this is an abstract class
    # Note: abc_import is NOT added to builder_imports here because it's already added
    # at line 504 for the class itself, and will be deduplicated at line 521-564
    abc_import = ""  # Always empty - added separately in generate_class_code

    # Import BuilderBase
    builder_base_import = "from armodel.models.M2.builder_base import BuilderBase\n"

    # Import parent Builder class if exists
    parent_builder_import = ""
    if builder_parent:
        parent_class = builder_parent.replace("Builder", "")
        parent_import_path = get_type_import_path(parent_class, package_data)
        if parent_import_path:
            # Extract the import path and modify it to import the Builder
            # Current format: from armodel.models.M2.xxx.some_class import (SomeClass,)
            # Need: from armodel.models.M2.xxx.some_class import SomeClassBuilder
            parent_import_path = parent_import_path.replace(
                f"import (\n    {parent_class},\n)", f"import {parent_class}Builder"
            )
            parent_builder_import = f"{parent_import_path}\n"

    # Check if parent Builder is abstract
    parent_is_abstract = False
    if builder_parent:
        parent_class = builder_parent.replace("Builder", "")
        if parent_class in hierarchy_info and hierarchy_info[parent_class].get(
            "is_abstract", False
        ):
            parent_is_abstract = True

    # Build the Builder class (without imports - imports will be returned separately)
    code_parts = [
        class_def,
        f'    """Builder for {class_name} with fluent API."""',
        "",
        "    def __init__(self) -> None:",
        '        """Initialize builder with defaults."""',
        "        super().__init__()",
        f"        self._obj: {class_name} = {obj_init}",
        "",
        "".join(with_methods),
        "".join(list_methods),
        "",
        # Generate validation helper method (has access to imports in this context)
        _generate_validation_helper(),
        "",
    ]

    # Add build method - abstract classes get abstract method, others get regular method
    if is_abstract:
        code_parts.append("    @abstractmethod")
        code_parts.append(f"    def build(self) -> {class_name}:")
        code_parts.append(
            '        """Build and return the ' + class_name + ' instance (abstract)."""'
        )
        code_parts.append("        raise NotImplementedError")
    else:
        code_parts.append("    def build(self) -> " + class_name + ":")
        code_parts.append(
            '        """Build and return the ' + class_name + ' instance with validation."""'
        )
        code_parts.append("        self._validate_instance()")
        # Only call super().build() if parent is not abstract
        code_parts.append(
            "        super().build()"
            if builder_parent and not parent_is_abstract
            else "        pass"
        )
        code_parts.append("        return self._obj")

    # Combine builder imports
    builder_imports = abc_import + builder_base_import + parent_builder_import

    # Return tuple of (imports, builder_class_code)
    return (builder_imports, "\n".join(code_parts))


def generate_enum_code(enum_def: Dict[str, Any], json_file_path: str = "") -> str:
    """Generate Python Enum code from enum definition.

    Args:
        enum_def: Enum definition from enum JSON file
        json_file_path: Path to the JSON file containing the enum definition

    Returns:
        Generated Python Enum code as string
    """
    enum_name = enum_def["name"]
    literals = enum_def.get("literals", [])
    sources = enum_def.get("sources", [])

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"AUTOSAR {enum_name} enumeration."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Generate enum code as a class inheriting from AREnum only
    # The serialize() and deserialize() methods are inherited from AREnum
    code = f'''"""{docstring}"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class {enum_name}(AREnum):
    """AUTOSAR {enum_name} enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

'''

    # Deduplicate literals by name (keep first occurrence)
    seen_names = set()
    duplicates = []
    unique_literals = []

    for literal in literals:
        literal_name = literal["name"]
        if literal_name in seen_names:
            duplicates.append(literal_name)
        else:
            seen_names.add(literal_name)
            unique_literals.append(literal)

    # Warn about duplicates
    if duplicates:
        duplicate_set = set(duplicates)
        code += f"    # Note: {len(duplicate_set)} duplicate literal(s) found and removed: {', '.join(sorted(duplicate_set))}\n"

    # Generate enum members from unique literals
    for literal in unique_literals:
        literal_value = literal["name"]
        # Convert enum literal name to AUTOSAR XML format (UPPER-CASE-WITH-HYPHENS)
        # This ensures compatibility with AUTOSAR XML files that use this format
        autosar_xml_value = to_autosar_xml_format(literal_value)
        # Convert enum member name to UPPER_SNAKE_CASE with underscores between words
        literal_name = to_snake_case(literal_value).upper()
        code += f'    {literal_name} = "{autosar_xml_value}"\n'

    return code


def generate_primitive_type_base() -> str:
    """Generate the ARPrimitive base class code.

    Returns:
        Generated Python code as string
    """
    code = '''"""ARPrimitive base class for all AUTOSAR primitive types."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class ARPrimitive(ARObject):
    """Base class for all AUTOSAR primitive types.

    All primitive types (String, Integer, Float, etc.) inherit from this class.
    Provides common functionality for value wrapping and serialization.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self) -> None:
        """Initialize ARPrimitive."""
        super().__init__()
        self.value: Optional[Any] = None

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the primitive to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this primitive
        """
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        if self.value is not None:
            elem.text = str(self.value)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPrimitive":
        """Deserialize an XML element to an ARPrimitive instance.

        Automatically converts the text content to the appropriate Python type
        based on the python_type class attribute.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPrimitive instance
        """
        obj = cls()
        if element.text:
            # Convert to the appropriate Python type based on python_type
            if cls.python_type is str:
                obj.value = element.text
            elif cls.python_type is int:
                try:
                    obj.value = int(element.text)
                except ValueError:
                    obj.value = element.text  # Keep as string if conversion fails
            elif cls.python_type is float:
                try:
                    obj.value = float(element.text)
                except ValueError:
                    obj.value = element.text
            elif cls.python_type is bool:
                obj.value = element.text.lower() in ('true', '1', 'yes')
            else:
                obj.value = element.text
        return obj

    def __str__(self) -> str:
        """Return string representation of the primitive value."""
        return str(self.value) if self.value is not None else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}({self.value!r})"
'''
    return code


def generate_enumeration_type_base() -> str:
    """Generate the AREnum base class code.

    Returns:
        Generated Python code as string
    """
    code = '''"""AREnum base class for all AUTOSAR enumeration types."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class AREnum(ARObject):
    """Base class for all AUTOSAR enumeration types.

    All enumeration types inherit from this class.
    Provides common functionality for enum value serialization.
    """

    def __init__(self) -> None:
        """Initialize AREnum."""
        super().__init__()

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the enum to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this enum value
        """
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        # Get the value from the enum
        if hasattr(self, 'value'):
            elem.text = str(self.value)
        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AREnum":
        """Deserialize an XML element to an AREnum instance.

        This base method should be overridden by concrete enum classes
        to handle matching against specific enum members.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AREnum instance

        Raises:
            ValueError: If element is empty
        """
        if element.text:
            # Fallback: create a custom instance
            # Subclasses should override this to match against their members
            text = element.text.strip()
            obj = cls.__new__(cls)
            object.__setattr__(obj, '_value_', text)
            # Initialize parent class (ARObject)
            super(cls, obj).__init__()
            return obj
        raise ValueError(f"Cannot deserialize {{cls.__name__}} from empty element")

    def __str__(self) -> str:
        """Return string representation of the enum value."""
        return str(self.value) if hasattr(self, 'value') else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}.{self.name if hasattr(self, 'name') else self.value}"
'''
    return code


def _generate_serialize_method(
    class_name: str,
    attribute_types: Dict[str, Dict[str, Any]],
    parent_class: Optional[str],
    package_data: Dict[str, Dict[str, Any]],
) -> str:
    """Generate optimized serialize() method for a class.

    This method generates a custom serialize() implementation that:
    1. Serializes attributes directly without reflection
    2. Reuses parent class serialize() for inherited attributes
    3. Handles lists, primitives, objects, and ARRef types efficiently

    Args:
        class_name: Name of the class
        attribute_types: Dictionary of attribute information
        parent_class: Name of parent class (if any)
        package_data: Package data dictionary

    Returns:
        Generated serialize() method code
    """
    code = f'''    def serialize(self) -> ET.Element:
        """Serialize {class_name} to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

'''

    # If class has a parent class, call parent's serialize first
    # to handle inherited attributes, then serialize own attributes
    if parent_class:
        code += f"""        # First, call parent's serialize to handle inherited attributes
        parent_elem = super({class_name}, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

"""

    # Generate code to serialize each attribute
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Get Python identifier
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
            # Convert attribute name to snake_case then to XML tag (UPPER-CASE-WITH-HYPHENS)
            snake_name = to_snake_case(attr_name)
            xml_tag = snake_name.upper().replace("_", "-")
            # Add -TREF or -REF suffix for reference attributes with multiplicity != "*"
            # Container elements (multiplicity "*") should not have -REF suffix
            # Note: iref kind is handled separately below and doesn't get -REF suffix
            if is_ref and multiplicity != "*" and kind != "iref":
                # Use the kind field from JSON to determine the suffix
                # "tref" -> -TREF, "ref" -> -REF
                if kind == "tref":
                    xml_tag = f"{xml_tag}-TREF"
                else:
                    xml_tag = f"{xml_tag}-REF"

            # Convert "any (xxx)" types to "Any" for generation
            effective_type = attr_type
            if attr_type.startswith("any ("):
                effective_type = "Any"

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # Handle xml_attribute - serialize as XML attribute, not child element
            if kind == "xml_attribute" or decorator_name == "xml_attribute":
                # Get decorator params if present for custom XML attribute name
                decorator_params = attr_info.get("decorator_params", None)
                if decorator_params:
                    xml_attr_tag = decorator_params  # Use custom attribute name from decorator
                else:
                    xml_attr_tag = xml_tag  # Use auto-converted name
                code += f'''        # Serialize {python_name} as XML attribute
        if self.{python_name} is not None:
            elem.attrib["{xml_attr_tag}"] = str(self.{python_name})

'''
            elif decorator_name == "lang_abbr":
                # Handle lang_abbr - serialize with custom XML attribute name
                xml_attr_name = attr_info.get("decorator_params", attr_name.upper())
                code += f'''        # Serialize {python_name} as language abbreviation XML attribute
        if self.{python_name} is not None:
            elem.attrib["{xml_attr_name}"] = str(self.{python_name})

'''
            elif kind == "iref":
                # Handle iref kind - instance reference with special wrapper
                # The outer wrapper is attribute name + -IREF
                # Check decorator for flatten parameter
                decorator_name = attr_info.get("decorator_name")
                decorator_params = attr_info.get("decorator_params")
                
                # Determine if this should be flattened based on decorator parameter
                should_flatten = False
                if decorator_name == "instance_ref" and decorator_params:
                    # Parse decorator params (format: "flatten=True" or "flatten=False")
                    if "flatten=True" in decorator_params:
                        should_flatten = True
                    elif "flatten=False" in decorator_params:
                        should_flatten = False

                iref_wrapper_tag = f"{xml_tag}-IREF"
                if should_flatten:
                    # Flattened type: flatten children directly into iref wrapper
                    if multiplicity == "*":
                        # List type - check if not empty
                        code += f'''        # Serialize {python_name} (list of instance references with wrapper "{iref_wrapper_tag}")
        if self.{python_name}:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

'''
                    else:
                        # Single item type
                        code += f'''        # Serialize {python_name} (instance reference with wrapper "{iref_wrapper_tag}")
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

'''
                else:
                    # Non-flattened type: wrap in its own element
                    if multiplicity == "*":
                        # List type - check if not empty
                        code += f'''        # Serialize {python_name} (list of instance references with wrapper "{iref_wrapper_tag}")
        if self.{python_name}:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

'''
                    else:
                        # Single item type
                        code += f'''        # Serialize {python_name} (instance reference with wrapper "{iref_wrapper_tag}")
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

'''
            elif multiplicity == "*":
                # List type
                # Check if the XML tag ends with "S" (plural form like PACKAGES, ELEMENTS)
                # If so, it's a container element and we need to create a wrapper
                if xml_tag.endswith("S"):
                    # Check if ref_conditional decorator is present
                    decorator_name = attr_info.get("decorator_name")
                    if decorator_name == "ref_conditional":
                        # Use ref_conditional pattern: container stays as-is, each item wrapped in -REF-CONDITIONAL
                        container_tag = attr_info.get("decorator_params", xml_tag)
                        singular = container_tag[:-1]  # Remove trailing S
                        conditional_tag = f"{singular}-REF-CONDITIONAL"
                        ref_tag = f"{singular}-REF"
                    elif decorator_name == "xml_element_name":
                        # Parse decorator params: can be single value or multi-level path separated by '/'
                        # Examples: "PROVIDED-ENTRYS" or "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF"
                        decorator_params = attr_info.get("decorator_params", xml_tag)
                        if isinstance(decorator_params, str) and "/" in decorator_params:
                            # Multi-level nesting: split on '/' to get all levels
                            tag_levels = [level.strip() for level in decorator_params.split("/")]
                            container_tag = tag_levels[0]  # Outermost container
                            child_tag = tag_levels[-1]  # Innermost tag for individual items
                            inner_tags = tag_levels[1:-1]  # Intermediate nesting levels (if any)
                        else:
                            # Single parameter: just container tag
                            container_tag = (
                                decorator_params if isinstance(decorator_params, str) else xml_tag
                            )
                            child_tag = None
                            inner_tags = []
                    else:
                        # Container element (e.g., AR-PACKAGES, ELEMENTS, USE-INSTEAD-REFS)
                        # For reference lists (is_ref=True), the container tag should be singular + -REFS
                        # For non-reference lists, the container tag is the plural form (e.g., LIFE-CYCLE-INFOS)
                        container_tag = xml_tag
                        child_tag = None
                        inner_tags = []
                        if is_ref:
                            # For reference lists, the container tag is singular form + -REFS
                            # e.g., USE-INSTEADS -> USE-INSTEAD-REFS
                            # Child tag is singular form + -REF
                            singular = xml_tag[:-1]  # Remove trailing 'S'
                            container_tag = f"{singular}-REFS"

                    code += f'''        # Serialize {python_name} (list to container "{container_tag}")
        if self.{python_name}:
            wrapper = ET.Element("{container_tag}")
            for item in self.{python_name}:
                serialized = SerializationHelper.serialize_item(item, "{effective_type}")
                if serialized is not None:
'''

                    # For reference lists, wrap each item in a child element with -REF suffix
                    # For primitive/enum lists, wrap each item in a child element with singular tag name
                    # For complex object lists, append the serialized item directly (it already has correct tag)
                    if is_ref:
                        # Check if ref_conditional decorator is present
                        decorator_name = attr_info.get("decorator_name")
                        if decorator_name == "ref_conditional":
                            # Wrap each reference in -REF-CONDITIONAL containing the actual -REF
                            code += f'''                    # Wrap in {conditional_tag}
                    conditional = ET.Element("{conditional_tag}")
                    ref_elem = ET.Element("{ref_tag}")
                    if hasattr(serialized, 'attrib'):
                        ref_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        ref_elem.text = serialized.text
                    for child in serialized:
                        ref_elem.append(child)
                    conditional.append(ref_elem)
                    wrapper.append(conditional)
'''
                        # Use the child_tag from decorator if specified, otherwise generate from xml_tag
                        elif child_tag:
                            # Multi-level nesting: create nested wrappers for intermediate levels
                            if inner_tags:
                                # Start with the innermost child element
                                code += f'''                    child_elem = ET.Element("{child_tag}")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
'''
                                # Create nested wrappers in reverse order (innermost to outermost)
                                for tag in reversed(inner_tags):
                                    code += f'''                    nested_wrapper = ET.Element("{tag}")
                    nested_wrapper.append(child_elem)
                    child_elem = nested_wrapper
'''
                                # Append the outermost nested wrapper to the main wrapper
                                code += """                    wrapper.append(child_elem)
"""
                            else:
                                # Single-level nesting
                                code += f'''                    child_elem = ET.Element("{child_tag}")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
'''
                        else:
                            # Generate child tag from xml_tag
                            singular = xml_tag[:-1]  # Remove trailing 'S'
                            # Use the kind field from JSON to determine the suffix
                            # "tref" -> -TREF, "ref" -> -REF
                            if kind == "tref":
                                generated_child_tag = f"{singular}-TREF"
                            else:
                                generated_child_tag = f"{singular}-REF"
                            code += f'''                    child_elem = ET.Element("{generated_child_tag}")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
'''
                    elif is_primitive_type(attr_type, package_data) or is_enum_type(
                        attr_type, package_data
                    ):
                        # Primitive or enum type - wrap in child element with singular tag name
                        singular = xml_tag[:-1]  # Remove trailing 'S'
                        code += f'''                    child_elem = ET.Element("{singular}")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
'''
                    else:
                        # Complex object type - append directly (already has correct tag)
                        code += """                    wrapper.append(serialized)
"""

                    code += """            if len(wrapper) > 0:
                elem.append(wrapper)

"""
                else:
                    # Non-container list type (multiple instances of the same element)
                    # Check if this is an l_prefix attribute
                    if decorator_name == "lang_prefix":
                        # lang_prefix attributes use the tag from decorator_params (e.g., L-1, L-10)
                        lang_prefix_tag = attr_info.get("decorator_params", "")
                        code += f'''        # Serialize {python_name} (list with lang_prefix "{lang_prefix_tag}")
        for item in self.{python_name}:
            serialized = SerializationHelper.serialize_item(item, "{effective_type}")
            if serialized is not None:
                # For lang_prefix lists, wrap each item in the lang_prefix tag
                wrapped = ET.Element("{lang_prefix_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

'''
                    else:
                        # Regular non-container list
                        code += f'''        # Serialize {python_name} (list)
        for item in self.{python_name}:
            serialized = SerializationHelper.serialize_item(item, "{effective_type}")
            if serialized is not None:
                # For non-container lists, wrap with correct tag
                wrapped = ET.Element("{xml_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

'''
            else:
                # Single value type
                code += f'''        # Serialize {python_name}
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("{xml_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

'''

    code += """        return elem

"""
    return code


def _generate_serialize_method_for_atp_variant(
    class_name: str,
    attribute_types: Dict[str, Dict[str, Any]],
    parent_class: Optional[str],
    package_data: Dict[str, Dict[str, Any]],
) -> str:
    """Generate serialize() method for atp_variant classes.

    This method generates a custom serialize() implementation that:
    1. Calls parent's serialize to handle inherited attributes
    2. Serializes own attributes to an inner element
    3. Wraps the inner element in VARIANTS/CONDITIONAL structure

    Args:
        class_name: Name of the class
        attribute_types: Dictionary of attribute information
        parent_class: Name of parent class (if any)
        package_data: Package data dictionary

    Returns:
        Generated serialize() method code
    """
    code = f'''    def serialize(self) -> ET.Element:
        """Serialize {class_name} to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

'''

    # If class has a parent class, call parent's serialize first
    if parent_class:
        code += f"""        # First, call parent's serialize to handle inherited attributes
        parent_elem = super({class_name}, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

"""

    # Create inner element for attributes
    code += """        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

"""

    # Generate code to serialize each attribute to inner element
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Get Python identifier
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
            # Convert attribute name to snake_case then to XML tag (UPPER-CASE-WITH-HYPHENS)
            snake_name = to_snake_case(attr_name)
            xml_tag = snake_name.upper().replace("_", "-")
            # Add -TREF or -REF suffix for reference attributes with multiplicity != "*"
            if is_ref and multiplicity != "*" and kind != "iref":
                if kind == "tref":
                    xml_tag = f"{xml_tag}-TREF"
                else:
                    xml_tag = f"{xml_tag}-REF"

            # Convert "any (xxx)" types to "Any" for generation
            effective_type = attr_type
            if attr_type.startswith("any ("):
                effective_type = "Any"

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # Handle xml_attribute - serialize as XML attribute, not child element
            if kind == "xml_attribute" or decorator_name == "xml_attribute":
                # Get decorator params if present for custom XML attribute name
                decorator_params = attr_info.get("decorator_params", None)
                if decorator_params:
                    xml_attr_tag = decorator_params  # Use custom attribute name from decorator
                else:
                    xml_attr_tag = xml_tag  # Use auto-converted name
                code += f'''        # Serialize {python_name} as XML attribute
        if self.{python_name} is not None:
            inner_elem.attrib["{xml_attr_tag}"] = str(self.{python_name})

'''
            elif decorator_name == "lang_abbr":
                # Handle lang_abbr - serialize with custom XML attribute name
                xml_attr_name = attr_info.get("decorator_params", attr_name.upper())
                code += f'''        # Serialize {python_name} as language abbreviation XML attribute
        if self.{python_name} is not None:
            inner_elem.attrib["{xml_attr_name}"] = str(self.{python_name})

'''
            elif kind == "iref":
                # Handle iref kind - instance reference with special wrapper
                flattened_iref_types = {
                    "PPortInCompositionInstanceRef",
                    "RPortInCompositionInstanceRef",
                }
                should_flatten = attr_type in flattened_iref_types
                iref_wrapper_tag = f"{xml_tag}-IREF"

                if should_flatten:
                    if multiplicity == "*":
                        code += f'''        # Serialize {python_name} (list of instance references with wrapper "{iref_wrapper_tag}")
        if self.{python_name}:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                for child in serialized:
                    iref_wrapper.append(child)
                inner_elem.append(iref_wrapper)

'''
                    else:
                        code += f'''        # Serialize {python_name} (instance reference with wrapper "{iref_wrapper_tag}")
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                for child in serialized:
                    iref_wrapper.append(child)
                inner_elem.append(iref_wrapper)

'''
                else:
                    if multiplicity == "*":
                        code += f'''        # Serialize {python_name} (list of instance references with wrapper "{iref_wrapper_tag}")
        if self.{python_name}:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                iref_wrapper.append(serialized)
                inner_elem.append(iref_wrapper)

'''
                    else:
                        code += f'''        # Serialize {python_name} (instance reference with wrapper "{iref_wrapper_tag}")
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                iref_wrapper = ET.Element("{iref_wrapper_tag}")
                iref_wrapper.append(serialized)
                inner_elem.append(iref_wrapper)

'''
            elif multiplicity == "*":
                # List type
                if xml_tag.endswith("S"):
                    container_tag = xml_tag
                    if is_ref:
                        singular = xml_tag[:-1]
                        container_tag = f"{singular}-REFS"

                    code += f'''        # Serialize {python_name} (list from container "{container_tag}")
        if self.{python_name}:
            container = ET.Element("{container_tag}")
            for item in self.{python_name}:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("{attr_type}", package_data):
                    # Simple primitive type
                    child = ET.Element("{xml_tag[:-1]}")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("{attr_type}", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

'''
                else:
                    if decorator_name == "lang_prefix":
                        lang_prefix_tag = attr_info.get("decorator_params", "")
                        code += f'''        # Serialize {python_name} (list with lang_prefix "{lang_prefix_tag}")
        for item in self.{python_name}:
            serialized = SerializationHelper.serialize_item(item, "{effective_type}")
            if serialized is not None:
                wrapped = ET.Element("{lang_prefix_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

'''
                    else:
                        code += f'''        # Serialize {python_name} (list)
        for item in self.{python_name}:
            serialized = SerializationHelper.serialize_item(item, "{effective_type}")
            if serialized is not None:
                wrapped = ET.Element("{xml_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

'''
            else:
                # Single value type
                code += f'''        # Serialize {python_name}
        if self.{python_name} is not None:
            serialized = SerializationHelper.serialize_item(self.{python_name}, "{effective_type}")
            if serialized is not None:
                wrapped = ET.Element("{xml_tag}")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

'''

    # Wrap inner element in atp_variant structure
    code += f"""        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "{class_name}")
        elem.append(wrapped)

        return elem

"""
    return code


def _generate_deserialize_method_for_atp_variant(
    class_name: str,
    attribute_types: Dict[str, Dict[str, Any]],
    parent_class: Optional[str],
    package_data: Dict[str, Dict[str, Any]],
) -> str:
    """Generate deserialize() method for atp_variant classes.

    This method generates a custom deserialize() implementation that:
    1. Calls parent's deserialize to handle inherited attributes
    2. Unwraps VARIANTS/CONDITIONAL structure to access attributes
    3. Parses own attributes from the unwrapped element

    Args:
        class_name: Name of the class
        attribute_types: Dictionary of attribute information
        parent_class: Name of parent class (if any)
        package_data: Package data dictionary

    Returns:
        Generated deserialize() method code
    """
    code = f'''    @classmethod
    def deserialize(cls, element: ET.Element) -> "{class_name}":
        """Deserialize XML element to {class_name} object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized {class_name} object
        """
'''

    # If class has a parent class, call parent's deserialize first
    if parent_class:
        code += f"""        # First, call parent's deserialize to handle inherited attributes
        obj = super({class_name}, cls).deserialize(element)

"""
    else:
        # No parent class to handle, create instance directly
        code += """        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

"""

    # Unwrap atp_variant structure
    code += f"""        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "{class_name}")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

"""

    # Generate code to parse each attribute from inner element
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            attr_type = attr_info["type"]
            multiplicity = attr_info["multiplicity"]
            is_ref = attr_info.get("is_ref", False)
            kind = attr_info.get("kind", "attribute")

            # Get Python identifier
            python_name = get_python_identifier_with_ref(attr_name, is_ref, multiplicity, kind)
            # Convert attribute name to snake_case then to XML tag (UPPER-CASE-WITH-HYPHENS)
            snake_name = to_snake_case(attr_name)
            xml_tag = snake_name.upper().replace("_", "-")
            # Add -TREF or -REF suffix for reference attributes with multiplicity != "*"
            if is_ref and multiplicity != "*" and kind != "iref":
                if kind == "tref":
                    xml_tag = f"{xml_tag}-TREF"
                else:
                    xml_tag = f"{xml_tag}-REF"

            # Convert "any (xxx)" types to "Any" for generation
            effective_type = attr_type
            if attr_type.startswith("any ("):
                effective_type = "Any"

            # Get decorator_name if present
            decorator_name = attr_info.get("decorator_name")

            # Handle xml_attribute - parse from XML attribute
            if kind == "xml_attribute" or decorator_name == "xml_attribute":
                # Get decorator params if present for custom XML attribute name
                decorator_params = attr_info.get("decorator_params", None)
                if decorator_params:
                    xml_attr_tag = decorator_params  # Use custom attribute name from decorator
                else:
                    xml_attr_tag = xml_tag  # Use auto-converted name
                code += f'''        # Parse {python_name} from XML attribute
        {python_name}_value = inner_elem.get("{xml_attr_tag}")
        if {python_name}_value is not None:
            {_generate_value_extraction_code(effective_type, "{python_name}_value", package_data, python_name, is_ref, kind)}
            obj.{python_name} = {python_name}_value

'''
            elif kind == "iref":
                # Handle iref kind - instance reference with special wrapper
                # Flattened types have their children directly inside the iref wrapper, not wrapped in their own element
                # These instance reference types contain direct child elements like CONTEXT-COMPOSITION-REF,
                # CONTEXT-PORT-REF, TARGET-DATA-PROTOTYPE-REF, etc.
                flattened_iref_types = {
                    # SWComponentTemplate Composition InstanceRefs
                    "PPortInCompositionInstanceRef",
                    "RPortInCompositionInstanceRef",
                    "ComponentInCompositionInstanceRef",
                    "PortInCompositionTypeInstanceRef",
                    "InstanceEventInCompositionInstanceRef",
                    # SystemTemplate InstanceRefs
                    "ComponentInSystemInstanceRef",
                    "OperationInSystemInstanceRef",
                    "VariableDataPrototypeInSystemInstanceRef",
                    "TriggerInSystemInstanceRef",
                    "PortGroupInSystemInstanceRef",
                    # SWComponentTemplate Components InstanceRefs
                    "VariableInAtomicSwcInstanceRef",
                    "RVariableInAtomicSwcInstanceRef",
                    "RModeInAtomicSwcInstanceRef",
                    "InnerPortGroupInCompositionInstanceRef",
                    "TriggerInAtomicSwcInstanceRef",
                    "RTriggerInAtomicSwcInstanceRef",
                    "PTriggerInAtomicSwcTypeInstanceRef",
                    "OperationInAtomicSwcInstanceRef",
                    "ROperationInAtomicSwcInstanceRef",
                    "POperationInAtomicSwcInstanceRef",
                    "RModeGroupInAtomicSWCInstanceRef",
                    "PModeGroupInAtomicSwcInstanceRef",
                    "ModeGroupInAtomicSwcInstanceRef",
                    # SWComponentTemplate SwcInternalBehavior DataElements InstanceRefs
                    "ParameterInAtomicSWCTypeInstanceRef",
                    "VariableInAtomicSWCTypeInstanceRef",
                    # SWComponentTemplate PortInterface InstanceRefs
                    "ApplicationCompositeElementInPortInterfaceInstanceRef",
                }
                should_flatten = attr_type in flattened_iref_types
                iref_wrapper_tag = f"{xml_tag}-IREF"

                if should_flatten:
                    if multiplicity == "*":
                        code += f'''        # Parse {python_name} (list of instance references from wrapper "{iref_wrapper_tag}")
        obj.{python_name} = []
        wrapper = SerializationHelper.find_child_element(inner_elem, "{iref_wrapper_tag}")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            {python_name}_value = SerializationHelper.deserialize_by_tag(wrapper, "{effective_type}")
            obj.{python_name} = {python_name}_value

'''
                    else:
                        code += f'''        # Parse {python_name} (instance reference from wrapper "{iref_wrapper_tag}")
        wrapper = SerializationHelper.find_child_element(inner_elem, "{iref_wrapper_tag}")
        if wrapper is not None:
            {python_name}_value = SerializationHelper.deserialize_by_tag(wrapper, "{effective_type}")
            obj.{python_name} = {python_name}_value

'''
                else:
                    if multiplicity == "*":
                        code += f'''        # Parse {python_name} (list of instance references from wrapper "{iref_wrapper_tag}")
        obj.{python_name} = []
        wrapper = SerializationHelper.find_child_element(inner_elem, "{iref_wrapper_tag}")
        if wrapper is not None:
            children = list(wrapper)
            if children:
                inner = children[0]
                {_generate_value_extraction_code(effective_type, "inner", package_data, python_name, is_ref, kind)}
                obj.{python_name} = {python_name}_value

'''
                    else:
                        code += f'''        # Parse {python_name} (instance reference from wrapper "{iref_wrapper_tag}")
        wrapper = SerializationHelper.find_child_element(inner_elem, "{iref_wrapper_tag}")
        if wrapper is not None:
            children = list(wrapper)
            if children:
                inner = children[0]
                {_generate_value_extraction_code(effective_type, "inner", package_data, python_name, is_ref, kind)}
                obj.{python_name} = {python_name}_value

'''
            elif multiplicity == "*":
                # List type
                if xml_tag.endswith("S"):
                    # Check if ref_conditional decorator is present
                    decorator_name = attr_info.get("decorator_name")
                    # Initialize tag variables
                    container_tag = xml_tag
                    child_tag = None
                    inner_tags = []
                    conditional_tag = None
                    ref_tag = None

                    if decorator_name == "ref_conditional":
                        # Use ref_conditional pattern: container stays as-is, each item wrapped in -REF-CONDITIONAL
                        container_tag = attr_info.get("decorator_params", xml_tag)
                        singular = container_tag[:-1]  # Remove trailing S
                        conditional_tag = f"{singular}-REF-CONDITIONAL"
                        ref_tag = f"{singular}-REF"
                    elif decorator_name == "xml_element_name":
                        # Parse decorator params: can be single value or multi-level path separated by '/'
                        # Examples: "PROVIDED-ENTRYS" or "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA/CAN-ENTER-EXCLUSIVE-AREA-REF"
                        decorator_params = attr_info.get("decorator_params", xml_tag)
                        if isinstance(decorator_params, str) and "/" in decorator_params:
                            # Multi-level nesting: split on '/' to get all levels
                            tag_levels = [level.strip() for level in decorator_params.split("/")]
                            container_tag = tag_levels[0]  # Outermost container
                            child_tag = tag_levels[-1]  # Innermost tag for individual items
                            inner_tags = tag_levels[1:-1]  # Intermediate nesting levels (if any)
                        else:
                            # Single parameter: just container tag
                            container_tag = (
                                decorator_params if isinstance(decorator_params, str) else xml_tag
                            )
                            child_tag = None
                            inner_tags = []
                    else:
                        if is_ref:
                            singular = xml_tag[:-1]
                            container_tag = f"{singular}-REFS"

                    code += f'''        # Parse {python_name} (list from container "{container_tag}")
        obj.{python_name} = []
        container = SerializationHelper.find_child_element(inner_elem, "{container_tag}")'''

                    # Add navigation through nested levels if inner_tags is not empty
                    if inner_tags:
                        code += """        # Navigate through nested container levels"""
                        for inner_tag in inner_tags:
                            code += f'''
        if container is not None:
            container = SerializationHelper.find_child_element(container, "{inner_tag}")'''

                    # Generate the child parsing code based on decorator type
                    if decorator_name == "ref_conditional":
                        # Generate ref_conditional specific code
                        ref_conditional_code = f'''
        if container is not None:
            for child in container:
                if is_ref:
                    # Unwrap -REF-CONDITIONAL to extract the inner -REF
                    child_element_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_element_tag == "{conditional_tag}":
                        ref_child = SerializationHelper.find_child_element(child, "{ref_tag}")
                        if ref_child is not None:
                            child_value = ARRef.deserialize(ref_child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("{attr_type}", package_data):
                    child_value = child.text
                elif is_enum_type("{attr_type}", package_data):
                    child_value = {attr_type}.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.{python_name}.append(child_value)

'''
                        code += ref_conditional_code
                    else:
                        # Generate standard reference parsing code
                        ref_code = f'''
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "{child_tag}":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("{attr_type}", package_data):
                    child_value = child.text
                elif is_enum_type("{attr_type}", package_data):
                    child_value = {attr_type}.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.{python_name}.append(child_value)

'''
                        code += ref_code
                else:
                    if decorator_name == "lang_prefix":
                        lang_prefix_tag = attr_info.get("decorator_params", "")
                        code += f'''        # Parse {python_name} (list with lang_prefix "{lang_prefix_tag}")
        obj.{python_name} = []
        for child in SerializationHelper.find_all_child_elements(inner_elem, "{lang_prefix_tag}"):
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name}.append({python_name}_value)

'''
                    else:
                        code += f'''        # Parse {python_name} (list)
        obj.{python_name} = []
        for child in SerializationHelper.find_all_child_elements(inner_elem, "{xml_tag}"):
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name}.append({python_name}_value)

'''
            else:
                # Single value type
                code += f'''        # Parse {python_name}
        child = SerializationHelper.find_child_element(inner_elem, "{xml_tag}")
        if child is not None:
            {_generate_value_extraction_code(effective_type, "child", package_data, python_name, is_ref)}
            obj.{python_name} = {python_name}_value

'''

    code += """        return obj

"""
    return code


def generate_primitive_code(
    primitive_def: Dict[str, Any],
    package_data: Optional[Dict[str, Dict[str, Any]]] = None,
    json_file_path: str = "",
) -> str:
    """Generate Python primitive type definition from primitive definition.

    Args:
        primitive_def: Primitive definition from primitive JSON file
        package_data: Package data dictionary for type resolution
        json_file_path: Path to the JSON file containing the primitive definition

    Returns:
        Generated Python code as string
    """
    if package_data is None:
        package_data = {}

    primitive_name = primitive_def["name"]
    note = primitive_def.get("note", "")
    sources = primitive_def.get("sources", [])
    attributes = primitive_def.get("attributes", {})

    # Build docstring with PDF references and JSON file path
    docstring_lines = [f"{primitive_name} AUTOSAR primitive type."]

    # Add PDF file references if available
    if sources:
        docstring_lines.append("")
        docstring_lines.append("References:")
        for source in sources:
            pdf_file = source.get("pdf_file", "N/A")
            page_number = source.get("page_number", "N/A")
            docstring_lines.append(f"  - {pdf_file} (page {page_number})")

    # Add JSON file path if available
    if json_file_path:
        docstring_lines.append("")
        docstring_lines.append(f"JSON Source: {json_file_path}")

    docstring = "\n".join(docstring_lines)

    # Determine Python type mapping
    primitive_type_map = {
        "String": "str",
        "Integer": "int",
        "Float": "float",
        "Boolean": "bool",
        "Numerical": "str",  # Complex numerical representation
        "PositiveInteger": "str",  # Can be hex/octal/binary
        "Limit": "str",  # Special limit representation
        "Ref": "str",  # Reference string
        "CIdentifier": "str",
        "NameToken": "str",
        "Identifier": "str",
        "DateTime": "str",
        "TimeValue": "float",
        "AlignmentType": "str",
        # Add more mappings as needed
    }

    python_type = primitive_type_map.get(primitive_name, "str")

    # Collect imports needed for attributes
    enum_imports = set()
    primitive_imports = set()

    # Process attributes to determine types and imports
    attribute_types = {}
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info["type"]
        multiplicity = attr_info["multiplicity"]
        kind = attr_info.get("kind", "attribute")
        is_ref = attr_info.get("is_ref", False)

        # Determine Python type for the attribute
        if is_primitive_type(attr_type, package_data):
            attribute_type = get_python_type(attr_type, multiplicity, package_data, False, kind)
            primitive_imports.add(attr_type)
        elif is_enum_type(attr_type, package_data):
            attribute_type = get_python_type(attr_type, multiplicity, package_data, False, kind)
            enum_imports.add(attr_type)
        else:
            # Class type
            attribute_type = get_python_type(attr_type, multiplicity, package_data, is_ref, kind)

        attribute_types[attr_name] = {
            "type": attribute_type,
            "multiplicity": multiplicity,
            "original_type": attr_type,
            "kind": attr_info.get("kind", "attribute"),
        }

    # Build imports section
    import_statements = []
    import_statements.append("from __future__ import annotations")
    import_statements.append("from typing import TYPE_CHECKING, Optional")
    import_statements.append("import xml.etree.ElementTree as ET")
    import_statements.append("")
    import_statements.append(
        "from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive"
    )

    # Add enum imports
    if enum_imports:
        import_statements.append("")
        # Import each enum from its specific module file to avoid circular imports
        for enum_name in sorted(enum_imports):
            enum_snake_name = to_snake_case(enum_name)
            import_statements.append(
                f"from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.{enum_snake_name} import ("
            )
            import_statements.append(f"    {enum_name},")
            import_statements.append(")")

    # Add primitive imports
    if primitive_imports:
        import_statements.append("")
        # Import each primitive from its specific module file to avoid circular imports
        for prim_name in sorted(primitive_imports):
            prim_snake_name = to_snake_case(prim_name)
            import_statements.append(
                f"from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.{prim_snake_name} import ("
            )
            import_statements.append(f"    {prim_name},")
            import_statements.append(")")

    # Generate primitive type code as a class inheriting from ARPrimitive
    # Note: deserialize() is inherited from ARPrimitive base class
    code = f'''"""{docstring}"""

{chr(10).join(import_statements)}

# {note}
class {primitive_name}(ARPrimitive):
    """AUTOSAR {primitive_name} primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = {python_type}
    """The underlying Python type for this primitive."""

'''

    # Add class-level type annotations for attributes
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            python_name, _ = get_python_identifier(attr_name)
            code += f"    {python_name}: {attr_info['type']}\n"
        code += "\n"

    # Build __init__ signature
    init_params = [f"value: Optional[{python_type}] = None"]
    for attr_name, attr_info in attribute_types.items():
        python_name, _ = get_python_identifier(attr_name)
        init_params.append(f"{python_name}: {attr_info['type']} = None")

    code += f'''    def __init__(self, {", ".join(init_params)}) -> None:
        """Initialize {primitive_name}.

        Args:
            value: The primitive value
'''

    # Add docstring for attribute parameters
    for attr_name, attr_info in attribute_types.items():
        python_name, _ = get_python_identifier(attr_name)
        code += f"            {python_name}: {attr_name}\n"

    code += '''        """
        super().__init__()
        self.value: Optional[{}] = value
'''.format(python_type)

    # Initialize attributes
    if attribute_types:
        for attr_name, attr_info in attribute_types.items():
            python_name, _ = get_python_identifier(attr_name)
            code += f"        self.{python_name}: {attr_info['type']} = {python_name}\n"

    return code
