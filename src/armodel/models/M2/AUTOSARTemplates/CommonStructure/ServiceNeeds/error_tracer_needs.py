"""ErrorTracerNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 263)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 832)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)


class ErrorTracerNeeds(ServiceNeeds):
    """AUTOSAR ErrorTracerNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    traced_failures: list[TracedFailure]
    def __init__(self) -> None:
        """Initialize ErrorTracerNeeds."""
        super().__init__()
        self.traced_failures: list[TracedFailure] = []
    def serialize(self) -> ET.Element:
        """Serialize ErrorTracerNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ErrorTracerNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize traced_failures (list to container "TRACED-FAILURES")
        if self.traced_failures:
            wrapper = ET.Element("TRACED-FAILURES")
            for item in self.traced_failures:
                serialized = ARObject._serialize_item(item, "TracedFailure")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ErrorTracerNeeds":
        """Deserialize XML element to ErrorTracerNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ErrorTracerNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ErrorTracerNeeds, cls).deserialize(element)

        # Parse traced_failures (list from container "TRACED-FAILURES")
        obj.traced_failures = []
        container = ARObject._find_child_element(element, "TRACED-FAILURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.traced_failures.append(child_value)

        return obj



class ErrorTracerNeedsBuilder:
    """Builder for ErrorTracerNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ErrorTracerNeeds = ErrorTracerNeeds()

    def build(self) -> ErrorTracerNeeds:
        """Build and return ErrorTracerNeeds object.

        Returns:
            ErrorTracerNeeds instance
        """
        # TODO: Add validation
        return self._obj
