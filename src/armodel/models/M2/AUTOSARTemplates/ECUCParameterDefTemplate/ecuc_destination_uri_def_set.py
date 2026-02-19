"""EcucDestinationUriDefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucDestinationUriDefSet(ARElement):
    """AUTOSAR EcucDestinationUriDefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri_defs: list[EcucDestinationUriDef]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriDefSet."""
        super().__init__()
        self.destination_uri_defs: list[EcucDestinationUriDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDefSet":
        """Deserialize XML element to EcucDestinationUriDefSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDefSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_uri_defs (list)
        obj.destination_uri_defs = []
        for child in ARObject._find_all_child_elements(element, "DESTINATION-URI-DEFS"):
            destination_uri_defs_value = ARObject._deserialize_by_tag(child, "EcucDestinationUriDef")
            obj.destination_uri_defs.append(destination_uri_defs_value)

        return obj



class EcucDestinationUriDefSetBuilder:
    """Builder for EcucDestinationUriDefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDefSet = EcucDestinationUriDefSet()

    def build(self) -> EcucDestinationUriDefSet:
        """Build and return EcucDestinationUriDefSet object.

        Returns:
            EcucDestinationUriDefSet instance
        """
        # TODO: Add validation
        return self._obj
