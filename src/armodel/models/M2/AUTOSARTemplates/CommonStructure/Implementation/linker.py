"""Linker AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Linker(Identifiable):
    """AUTOSAR Linker."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    name: Optional[String]
    options: Optional[String]
    vendor: Optional[String]
    version: Optional[String]
    def __init__(self) -> None:
        """Initialize Linker."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Linker":
        """Deserialize XML element to Linker object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Linker object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Linker, cls).deserialize(element)

        # Parse name
        child = ARObject._find_child_element(element, "NAME")
        if child is not None:
            name_value = child.text
            obj.name = name_value

        # Parse options
        child = ARObject._find_child_element(element, "OPTIONS")
        if child is not None:
            options_value = child.text
            obj.options = options_value

        # Parse vendor
        child = ARObject._find_child_element(element, "VENDOR")
        if child is not None:
            vendor_value = child.text
            obj.vendor = vendor_value

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

        return obj



class LinkerBuilder:
    """Builder for Linker."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Linker = Linker()

    def build(self) -> Linker:
        """Build and return Linker object.

        Returns:
            Linker instance
        """
        # TODO: Add validation
        return self._obj
