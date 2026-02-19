"""ConditionalChangeNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    byte: Optional[Integer]
    id: Optional[PositiveInteger]
    invert: Optional[Integer]
    mask: Optional[Integer]
    new_nad: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionalChangeNad":
        """Deserialize XML element to ConditionalChangeNad object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConditionalChangeNad object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse byte
        child = ARObject._find_child_element(element, "BYTE")
        if child is not None:
            byte_value = child.text
            obj.byte = byte_value

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse invert
        child = ARObject._find_child_element(element, "INVERT")
        if child is not None:
            invert_value = child.text
            obj.invert = invert_value

        # Parse mask
        child = ARObject._find_child_element(element, "MASK")
        if child is not None:
            mask_value = child.text
            obj.mask = mask_value

        # Parse new_nad
        child = ARObject._find_child_element(element, "NEW-NAD")
        if child is not None:
            new_nad_value = child.text
            obj.new_nad = new_nad_value

        return obj



class ConditionalChangeNadBuilder:
    """Builder for ConditionalChangeNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionalChangeNad = ConditionalChangeNad()

    def build(self) -> ConditionalChangeNad:
        """Build and return ConditionalChangeNad object.

        Returns:
            ConditionalChangeNad instance
        """
        # TODO: Add validation
        return self._obj
