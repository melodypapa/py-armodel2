"""EcucUriReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 81)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucUriReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri: Optional[EcucDestinationUriDef]
    def __init__(self) -> None:
        """Initialize EcucUriReferenceDef."""
        super().__init__()
        self.destination_uri: Optional[EcucDestinationUriDef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucUriReferenceDef":
        """Deserialize XML element to EcucUriReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucUriReferenceDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_uri
        child = ARObject._find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = ARObject._deserialize_by_tag(child, "EcucDestinationUriDef")
            obj.destination_uri = destination_uri_value

        return obj



class EcucUriReferenceDefBuilder:
    """Builder for EcucUriReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucUriReferenceDef = EcucUriReferenceDef()

    def build(self) -> EcucUriReferenceDef:
        """Build and return EcucUriReferenceDef object.

        Returns:
            EcucUriReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
