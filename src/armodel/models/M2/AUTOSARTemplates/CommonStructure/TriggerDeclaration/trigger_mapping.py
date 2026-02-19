"""TriggerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerMapping(ARObject):
    """AUTOSAR TriggerMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_trigger_ref: Optional[ARRef]
    second_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerMapping."""
        super().__init__()
        self.first_trigger_ref: Optional[ARRef] = None
        self.second_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerMapping":
        """Deserialize XML element to TriggerMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_trigger_ref
        child = ARObject._find_child_element(element, "FIRST-TRIGGER")
        if child is not None:
            first_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.first_trigger_ref = first_trigger_ref_value

        # Parse second_trigger_ref
        child = ARObject._find_child_element(element, "SECOND-TRIGGER")
        if child is not None:
            second_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.second_trigger_ref = second_trigger_ref_value

        return obj



class TriggerMappingBuilder:
    """Builder for TriggerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerMapping = TriggerMapping()

    def build(self) -> TriggerMapping:
        """Build and return TriggerMapping object.

        Returns:
            TriggerMapping instance
        """
        # TODO: Add validation
        return self._obj
