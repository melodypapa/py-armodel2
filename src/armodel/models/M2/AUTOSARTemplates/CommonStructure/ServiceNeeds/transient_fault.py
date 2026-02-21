"""TransientFault AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TransientFault(TracedFailure):
    """AUTOSAR TransientFault."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    possible_error_reactions: list[Any]
    def __init__(self) -> None:
        """Initialize TransientFault."""
        super().__init__()
        self.possible_error_reactions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TransientFault to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransientFault, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize possible_error_reactions (list to container "POSSIBLE-ERROR-REACTIONS")
        if self.possible_error_reactions:
            wrapper = ET.Element("POSSIBLE-ERROR-REACTIONS")
            for item in self.possible_error_reactions:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransientFault":
        """Deserialize XML element to TransientFault object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransientFault object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransientFault, cls).deserialize(element)

        # Parse possible_error_reactions (list from container "POSSIBLE-ERROR-REACTIONS")
        obj.possible_error_reactions = []
        container = ARObject._find_child_element(element, "POSSIBLE-ERROR-REACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.possible_error_reactions.append(child_value)

        return obj



class TransientFaultBuilder:
    """Builder for TransientFault."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransientFault = TransientFault()

    def build(self) -> TransientFault:
        """Build and return TransientFault object.

        Returns:
            TransientFault instance
        """
        # TODO: Add validation
        return self._obj
