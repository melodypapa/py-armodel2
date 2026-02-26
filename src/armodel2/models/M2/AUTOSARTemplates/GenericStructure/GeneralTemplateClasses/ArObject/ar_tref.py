"""ARTRef - AUTOSAR Type Reference.

This class represents AUTOSAR type references which are serialized as XML elements
with a DEST attribute pointing to the target type, an optional BASE attribute
specifying the base package/type, and text content containing the target path.

Example:
    <TYPE-TREF DEST="SW-BASE-TYPE" BASE="DataTypes">/Path/to/Target</TYPE-TREF>
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class ARTRef(ARRef):
    """Represents an AUTOSAR type reference to another element.

    Type references are serialized as XML elements with:
    - A DEST attribute specifying the target type
    - An optional BASE attribute specifying the base package/type
    - Text content containing the target path (e.g., "/Package/Element")

    Attributes:
        dest: The target type (e.g., "SW-BASE-TYPE")
        value: The target path reference
        base: The base package/type for the reference (e.g., "DataTypes")
    """

    def __init__(self, dest: Optional[str] = None, value: Optional[str] = None, base: Optional[str] = None) -> None:
        """Initialize an ARTRef with target type, path, and optional base.

        Args:
            dest: The DEST attribute value (target type)
            value: The reference target path
            base: The BASE attribute value (base package/type)
        """
        super().__init__(dest=dest, value=value, base=base)

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the type reference to an XML element.

        AUTOSAR type references are serialized as elements with:
        - DEST attribute (target type)
        - BASE attribute (base package/type, if present)
        - Text content (reference path)

        Args:
            namespace: Optional namespace (not used for references)

        Returns:
            XML element representing the type reference with DEST/BASE attributes and text content

        Example:
            <TYPE-TREF DEST="SW-BASE-TYPE" BASE="DataTypes">/Path/to/SwBaseType</TYPE-TREF>
        """
        # Create element - the tag name will be set by parent via _serialize_with_correct_tag
        # We use a temporary tag that will be replaced by parent
        elem = ET.Element("ARTREF")

        # Set DEST attribute if present
        if self._dest is not None:
            elem.set("DEST", self._dest)

        # Set BASE attribute if present
        if self._base is not None:
            elem.set("BASE", self._base)

        # Set text content (reference path)
        if self._value is not None:
            elem.text = self._value

        return elem

    @classmethod
    def deserialize(cls, element) -> ARTRef:
        """Deserialize an XML element to ARTRef.

        AUTOSAR type reference elements have:
        - DEST attribute (target type)
        - BASE attribute (base package/type, optional)
        - Text content (reference path)

        Args:
            element: XML element representing the type reference

        Returns:
            ARTRef instance with DEST/BASE attributes and text content

        Example:
            Input: <TYPE-TREF DEST="SW-BASE-TYPE" BASE="DataTypes">/Path/to/SwBaseType</TYPE-TREF>
            Output: ARTRef(dest="SW-BASE-TYPE", base="DataTypes", value="/Path/to/SwBaseType")
        """
        ref = cls()

        # Get DEST attribute
        ref.dest = element.get("DEST")

        # Get BASE attribute
        ref.base = element.get("BASE")

        # Get text content (reference path)
        # Strip leading/trailing whitespace from text content
        if element.text:
            ref.value = element.text.strip()
        else:
            ref.value = None

        return ref

    def __str__(self) -> str:
        """String representation of the type reference."""
        dest_str = self._dest or "Unknown"
        value_str = self._value or "None"
        base_str = self._base or "None"
        return f"ARTRef(dest={dest_str}, value={value_str}, base={base_str})"

    def __repr__(self) -> str:
        """Detailed representation of the type reference."""
        return self.__str__()