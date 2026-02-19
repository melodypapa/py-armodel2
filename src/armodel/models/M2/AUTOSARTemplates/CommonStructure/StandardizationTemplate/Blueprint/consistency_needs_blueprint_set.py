"""ConsistencyNeedsBlueprintSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Blueprint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)


class ConsistencyNeedsBlueprintSet(ARElement):
    """AUTOSAR ConsistencyNeedsBlueprintSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consistency_needses: list[ConsistencyNeeds]
    def __init__(self) -> None:
        """Initialize ConsistencyNeedsBlueprintSet."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsistencyNeedsBlueprintSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsistencyNeedsBlueprintSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consistency_needses (list to container "CONSISTENCY-NEEDSES")
        if self.consistency_needses:
            wrapper = ET.Element("CONSISTENCY-NEEDSES")
            for item in self.consistency_needses:
                serialized = ARObject._serialize_item(item, "ConsistencyNeeds")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeedsBlueprintSet":
        """Deserialize XML element to ConsistencyNeedsBlueprintSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeedsBlueprintSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsistencyNeedsBlueprintSet, cls).deserialize(element)

        # Parse consistency_needses (list from container "CONSISTENCY-NEEDSES")
        obj.consistency_needses = []
        container = ARObject._find_child_element(element, "CONSISTENCY-NEEDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consistency_needses.append(child_value)

        return obj



class ConsistencyNeedsBlueprintSetBuilder:
    """Builder for ConsistencyNeedsBlueprintSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsistencyNeedsBlueprintSet = ConsistencyNeedsBlueprintSet()

    def build(self) -> ConsistencyNeedsBlueprintSet:
        """Build and return ConsistencyNeedsBlueprintSet object.

        Returns:
            ConsistencyNeedsBlueprintSet instance
        """
        # TODO: Add validation
        return self._obj
