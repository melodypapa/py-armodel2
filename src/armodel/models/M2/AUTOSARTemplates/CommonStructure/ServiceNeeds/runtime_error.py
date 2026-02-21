"""RuntimeError AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 263)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 832)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class RuntimeError(TracedFailure):
    """AUTOSAR RuntimeError."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize RuntimeError."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize RuntimeError to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RuntimeError, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuntimeError":
        """Deserialize XML element to RuntimeError object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuntimeError object
        """
        # Delegate to parent class to handle inherited attributes
        return super(RuntimeError, cls).deserialize(element)



class RuntimeErrorBuilder:
    """Builder for RuntimeError."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuntimeError = RuntimeError()

    def build(self) -> RuntimeError:
        """Build and return RuntimeError object.

        Returns:
            RuntimeError instance
        """
        # TODO: Add validation
        return self._obj
