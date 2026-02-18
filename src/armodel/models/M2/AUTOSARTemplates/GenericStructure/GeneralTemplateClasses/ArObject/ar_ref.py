"""ARRef - AUTOSAR Reference Type.

This class represents AUTOSAR references which are serialized as XML elements
with a DEST attribute pointing to the target type and text content containing
the target path.

Example:
    <SW-ADDR-METHOD-REF DEST="SW-ADDR-METHOD">/Path/to/Target</SW-ADDR-METHOD-REF>
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    """

    def __init__(self, dest: Optional[str] = None, value: Optional[str] = None) -> None:
        """Initialize an ARRef with target type and path.

        Args:
            dest: The DEST attribute value (target type)
            value: The reference target path
        """
        super().__init__()
        self._dest: Optional[str] = dest
        self._value: Optional[str] = value

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

    @xml_attribute
    @property
    def DEST(self) -> Optional[str]:
        """XML attribute for DEST (serializes as DEST attribute)."""
        return self._dest

    @DEST.setter
    def DEST(self, value: Optional[str]) -> None:
        """Set the DEST attribute."""
        self._dest = value

    def serialize(self, namespace: str = "") -> str:
        """Serialize the reference to XML.

        Returns:
            The text content (reference path) of the reference element.

        Note:
            The DEST attribute is handled by the @xml_attribute decorator.
            The parent element's serialize() method handles wrapping this
            in the appropriate XML tag.
        """
        return self._value or ""

    @classmethod
    def deserialize(cls, element) -> ARRef:
        """Deserialize an XML element to ARRef.

        Args:
            element: XML element representing the reference

        Returns:
            ARRef instance with DEST attribute and text content
        """
        ref = cls()

        # Get DEST attribute
        ref.dest = element.get("DEST")

        # Get text content (reference path)
        ref.value = element.text if element.text else None

        return ref

    def __str__(self) -> str:
        """String representation of the reference."""
        dest_str = self._dest or "Unknown"
        value_str = self._value or "None"
        return f"ARRef(dest={dest_str}, value={value_str})"

    def __repr__(self) -> str:
        """Detailed representation of the reference."""
        return self.__str__()