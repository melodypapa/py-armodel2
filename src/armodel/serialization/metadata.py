"""
Metadata descriptors for declarative serialization.

This module provides the XMLMember descriptor class which allows
AUTOSAR model classes to declaratively specify their serialization
metadata.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    pass

T = TypeVar("T")


class XMLMember:
    """
    Descriptor for XML serialization metadata.

    This class replaces the tuple-based _xml_members approach with
    a rich, declarative metadata object that is more flexible and
    self-documenting.

    Attributes:
        xml_tag: The XML tag name (None to auto-generate from member name)
        is_attribute: True if this member is serialized as an XML attribute
        multiplicity: Multiplicity string ("0..1", "1", "0..*", "1..*", "*")
        element_class: The class type for list/element members (None for primitives)
        python_name: The Python attribute name (auto-detected from containing class)
        xml_name_override: Original XML tag if member name was modified (e.g., for Python keywords)
    """

    __slots__ = (
        "xml_tag",
        "is_attribute",
        "multiplicity",
        "element_class",
        "python_name",
        "xml_name_override",
        "_owner_class",
    )

    def __init__(
        self,
        xml_tag: str | None = None,
        *,
        is_attribute: bool = False,
        multiplicity: str = "0..1",
        element_class: type | None = None,
        xml_name_override: str | None = None,
    ) -> None:
        """
        Initialize XMLMember metadata.

        Args:
            xml_tag: XML tag name (None to auto-generate from member name)
            is_attribute: True if this should be an XML attribute (default: False)
            multiplicity: Multiplicity string:
                - "0..1": Optional single value
                - "1": Required single value
                - "0..1": Optional single value
                - "0..*", "*": Optional list (default)
                - "1..*": Required list
            element_class: Class type for list/element members (None for primitives)
            xml_name_override: Original XML tag name if member name was modified
        """
        self.xml_tag: str | None = xml_tag
        self.is_attribute: bool = is_attribute
        self.multiplicity: str = multiplicity
        self.element_class: type | None = element_class
        self.python_name: str = ""  # Will be set when added to a class
        self.xml_name_override: str | None = xml_name_override
        self._owner_class: type | None = None

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Called when the descriptor is assigned to a class attribute.

        Args:
            owner: The class that owns this descriptor
            name: The attribute name in the class
        """
        self.python_name = name
        self._owner_class = owner

        # Auto-generate xml_tag if not provided
        if self.xml_tag is None:
            self.xml_tag = self._python_to_xml_tag(name)

    def __get__(self, obj: Any, objtype: type | None = None) -> XMLMember:
        """
        Get the descriptor instance itself (not a value).

        This makes XMLMember a non-data descriptor - it doesn't store
        instance values, only provides metadata.

        Args:
            obj: The instance (ignored)
            objtype: The class type

        Returns:
            The XMLMember descriptor itself
        """
        return self

    def __set__(self, obj: Any, value: Any) -> None:
        """
        Prevent direct assignment to XMLMember attributes.

        XMLMember is metadata-only and should not be used to store values.
        """
        raise AttributeError(
            f"Cannot assign to XMLMember descriptor '{self.python_name}'. "
            f"This is metadata-only. Set the instance attribute directly."
        )

    @staticmethod
    def _python_to_xml_tag(name: str) -> str:
        """
        Convert a Python identifier to an XML tag name.

        Follows AUTOSAR naming conventions:
        - Converts snake_case to UPPER-CASE-WITH-HYPHENS
        - Example: 'short_name' -> 'SHORT-NAME'

        Args:
            name: Python identifier (snake_case)

        Returns:
            XML tag name (UPPER-CASE-WITH-HYPHENS)
        """
        # Remove trailing underscore if present (from Python keyword escape)
        if name.endswith("_"):
            name = name[:-1]

        # Convert to uppercase and replace underscores with hyphens
        return name.upper().replace("_", "-")

    def get_xml_tag(self) -> str:
        """
        Get the XML tag name for this member.

        Returns the override if set, otherwise the auto-generated tag.

        Returns:
            The XML tag name to use
        """
        if self.xml_name_override:
            return self.xml_name_override
        if self.xml_tag:
            return self.xml_tag
        # Auto-generate from python_name
        return self._python_to_xml_tag(self.python_name)

    def is_required(self) -> bool:
        """
        Check if this member is required.

        Returns:
            True if multiplicity indicates a required value
        """
        return self.multiplicity in ("1", "1..*")

    def is_list(self) -> bool:
        """
        Check if this member represents a list.

        Returns:
            True if multiplicity indicates a list
        """
        return self.multiplicity in ("*", "0..*", "1..*")

    def is_single_value(self) -> bool:
        """
        Check if this member represents a single value.

        Returns:
            True if multiplicity indicates a single value
        """
        return self.multiplicity in ("0..1", "1")

    def get_default_value(self) -> Any:
        """
        Get the default value for this member type.

        Returns:
            Default value based on multiplicity
        """
        if self.is_list():
            return []
        return None

    def validate(self, value: Any) -> bool:
        """
        Validate a value against this member's constraints.

        Args:
            value: The value to validate

        Returns:
            True if valid, False otherwise
        """
        if value is None:
            return not self.is_required()

        if self.is_list():
            if not isinstance(value, list):
                return False
            # Validate element class if specified
            if self.element_class:
                return all(isinstance(v, self.element_class) for v in value)
            return True

        else:  # Single value
            if self.element_class:
                return isinstance(value, self.element_class)
            return True

    def __repr__(self) -> str:
        """Return string representation of XMLMember."""
        return (
            f"XMLMember("
            f"python_name={self.python_name!r}, "
            f"xml_tag={self.get_xml_tag()!r}, "
            f"is_attribute={self.is_attribute}, "
            f"multiplicity={self.multiplicity!r}, "
            f"element_class={self.element_class.__name__ if self.element_class else None}"
            f")"
        )


def get_xml_metadata(obj: type | object) -> dict[str, XMLMember]:
    """
    Extract XML metadata from a class.

    This function retrieves the _xml_members dictionary from a class,
    handling both the new dict-based format and legacy tuple-based format.

    Args:
        obj: The class or instance to get metadata from

    Returns:
        Dictionary mapping member names to XMLMember instances
    """
    cls = obj if isinstance(obj, type) else type(obj)

    # Get _xml_members from class and all its parents (MRO)
    metadata: dict[str, XMLMember] = {}

    for parent_cls in reversed(cls.__mro__):
        if not hasattr(parent_cls, "_xml_members"):
            continue

        xml_members = parent_cls._xml_members

        # Handle legacy tuple format
        if isinstance(xml_members, list) and len(xml_members) > 0:
            if isinstance(xml_members[0], tuple):
                # Convert tuple format to XMLMember
                for member_tuple in xml_members:
                    if len(member_tuple) >= 4:
                        name = member_tuple[0]
                        xml_tag = member_tuple[1]
                        is_attribute = member_tuple[2]
                        is_list = member_tuple[3]
                        element_class = member_tuple[4] if len(member_tuple) > 4 else None

                        multiplicity = "*" if is_list else "0..1"

                        member = XMLMember(
                            xml_tag=xml_tag,
                            is_attribute=is_attribute,
                            multiplicity=multiplicity,
                            element_class=element_class,
                        )
                        # Set python_name explicitly since __set_name__ wasn't called
                        member.python_name = name
                        member._owner_class = parent_cls
                        metadata[name] = member
                continue

        # Handle dict format
        if isinstance(xml_members, dict):
            # Filter out non-XMLMember values (like the descriptor instances themselves)
            for name, member in xml_members.items():
                if isinstance(member, XMLMember):
                    # Create a new instance with the correct python_name
                    new_member = XMLMember(
                        xml_tag=member.xml_tag,
                        is_attribute=member.is_attribute,
                        multiplicity=member.multiplicity,
                        element_class=member.element_class,
                        xml_name_override=member.xml_name_override,
                    )
                    new_member.python_name = name
                    new_member._owner_class = parent_cls
                    metadata[name] = new_member

    return metadata


def create_xml_member_from_tuple(
    member_tuple: tuple[str, str | None, bool, bool, type | None],
    name: str | None = None,
) -> XMLMember:
    """
    Create an XMLMember instance from a legacy tuple.

    This helper function converts the old tuple-based metadata format
    to the new XMLMember format.

    Args:
        member_tuple: Legacy tuple (name, xml_tag, is_attribute, is_list, element_class)
        name: Optional name override (uses first tuple element if not provided)

    Returns:
        XMLMember instance
    """
    xml_tag = member_tuple[1]
    is_attribute = member_tuple[2]
    is_list = member_tuple[3]
    element_class = member_tuple[4] if len(member_tuple) > 4 else None

    multiplicity = "*" if is_list else "0..1"

    return XMLMember(
        xml_tag=xml_tag,
        is_attribute=is_attribute,
        multiplicity=multiplicity,
        element_class=element_class,
    )
