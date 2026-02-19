"""ARRef - AUTOSAR Reference Type.

This class represents AUTOSAR references which are serialized as XML elements
with a DEST attribute pointing to the target type and text content containing
the target path.

Example:
    <SW-ADDR-METHOD-REF DEST="SW-ADDR-METHOD">/Path/to/Target</SW-ADDR-METHOD-REF>
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization.decorators import xml_attribute

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class ARRef(ARObject):
    """Represents an AUTOSAR reference to another element.

    References are serialized as XML elements with:
    - A DEST attribute specifying the target type
    - Text content containing the target path (e.g., "/Package/Element")

    Attributes:
        dest: The target type (e.g., "SW-ADDR-METHOD")
        value: The target path reference
        base: The base package/type for the reference (e.g., "DataTypes")
    """

    def __init__(self, dest: Optional[str] = None, value: Optional[str] = None, base: Optional[str] = None) -> None:
        """Initialize an ARRef with target type and path.

        Args:
            dest: The DEST attribute value (target type)
            value: The reference target path
            base: The base package/type for the reference
        """
        super().__init__()
        self._dest: Optional[str] = dest
        self._value: Optional[str] = value
        self._base: Optional[str] = base

    @property
    def dest(self) -> Optional[str]:
        """Get the DEST attribute (target type)."""
        return self._dest

    @dest.setter
    def dest(self, value: Optional[str]) -> None:
        """Set the DEST attribute (target type)."""
        self._dest = value

    @property
    def value(self) -> Optional[str]:
        """Get the reference path value."""
        return self._value

    @value.setter
    def value(self, value: Optional[str]) -> None:
        """Set the reference path value."""
        self._value = value

    @property
    def base(self) -> Optional[str]:
        """Get the base package/type for the reference."""
        return self._base

    @base.setter
    def base(self, value: Optional[str]) -> None:
        """Set the base package/type for the reference."""
        self._base = value

    @xml_attribute
    @property
    def DEST(self) -> Optional[str]:
        """XML attribute for DEST (serializes as DEST attribute)."""
        return self._dest

    @xml_attribute
    @property
    def BASE(self) -> Optional[str]:
        """XML attribute for BASE (serializes as BASE attribute)."""
        return self._base

    @BASE.setter
    def BASE(self, value: Optional[str]) -> None:
        """Set the BASE attribute."""
        self._base = value

    @DEST.setter
    def DEST(self, value: Optional[str]) -> None:
        """Set the DEST attribute."""
        self._dest = value

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the reference to an XML element.

        AUTOSAR references are serialized as elements with:
        - DEST attribute (target type)
        - Text content (reference path)

        Args:
            namespace: Optional namespace (not used for references)

        Returns:
            XML element representing the reference with DEST attribute and text content

        Example:
            <PDU-REF DEST="PDU-TRIGGERING">/Path/to/PduTriggering</PDU-REF>
        """
        # Create element - the tag name will be set by parent via _serialize_with_correct_tag
        # We use a temporary tag that will be replaced by parent
        elem = ET.Element("ARREF")

        # Set BASE attribute if present
        if self._base is not None:
            elem.set("BASE", self._base)

        # Set DEST attribute if present
        if self._dest is not None:
            elem.set("DEST", self._dest)

        # Set text content (reference path)
        if self._value is not None:
            elem.text = self._value

        return elem

    @classmethod
    def deserialize(cls, element) -> ARRef:
        """Deserialize an XML element to ARRef.

        AUTOSAR reference elements have:
        - DEST attribute (target type)
        - Text content (reference path)

        Args:
            element: XML element representing the reference

        Returns:
            ARRef instance with DEST attribute and text content

        Example:
            Input: <PDU-REF DEST="PDU-TRIGGERING">/Path/to/PduTriggering</PDU-REF>
            Output: ARRef(dest="PDU-TRIGGERING", value="/Path/to/PduTriggering")
        """
        ref = cls()

        # Get BASE attribute
        ref.base = element.get("BASE")

        # Get DEST attribute
        ref.dest = element.get("DEST")

        # Get text content (reference path)
        # Strip leading/trailing whitespace from text content
        if element.text:
            ref.value = element.text.strip()
        else:
            ref.value = None

        return ref

    def __str__(self) -> str:
        """String representation of the reference."""
        dest_str = self._dest or "Unknown"
        value_str = self._value or "None"
        base_str = self._base or "None"
        return f"ARRef(dest={dest_str}, value={value_str}, base={base_str})"

    def __repr__(self) -> str:
        """Detailed representation of the reference."""
        return self.__str__()