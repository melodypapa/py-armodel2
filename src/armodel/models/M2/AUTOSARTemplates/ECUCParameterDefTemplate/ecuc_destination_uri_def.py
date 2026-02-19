"""EcucDestinationUriDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EcucDestinationUriDef(Identifiable):
    """AUTOSAR EcucDestinationUriDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri: Optional[Any]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriDef."""
        super().__init__()
        self.destination_uri: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDef":
        """Deserialize XML element to EcucDestinationUriDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_uri
        child = ARObject._find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = child.text
            obj.destination_uri = destination_uri_value

        return obj



class EcucDestinationUriDefBuilder:
    """Builder for EcucDestinationUriDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDef = EcucDestinationUriDef()

    def build(self) -> EcucDestinationUriDef:
        """Build and return EcucDestinationUriDef object.

        Returns:
            EcucDestinationUriDef instance
        """
        # TODO: Add validation
        return self._obj
