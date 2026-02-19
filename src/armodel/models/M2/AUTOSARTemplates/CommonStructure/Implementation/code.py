"""Code AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 130)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class Code(Identifiable):
    """AUTOSAR Code."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    artifacts: list[AutosarEngineeringObject]
    callback_headers: list[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize Code."""
        super().__init__()
        self.artifacts: list[AutosarEngineeringObject] = []
        self.callback_headers: list[ServiceNeeds] = []
    def serialize(self) -> ET.Element:
        """Serialize Code to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Code, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize artifacts (list to container "ARTIFACTS")
        if self.artifacts:
            wrapper = ET.Element("ARTIFACTS")
            for item in self.artifacts:
                serialized = ARObject._serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize callback_headers (list to container "CALLBACK-HEADERS")
        if self.callback_headers:
            wrapper = ET.Element("CALLBACK-HEADERS")
            for item in self.callback_headers:
                serialized = ARObject._serialize_item(item, "ServiceNeeds")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Code":
        """Deserialize XML element to Code object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Code object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Code, cls).deserialize(element)

        # Parse artifacts (list from container "ARTIFACTS")
        obj.artifacts = []
        container = ARObject._find_child_element(element, "ARTIFACTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.artifacts.append(child_value)

        # Parse callback_headers (list from container "CALLBACK-HEADERS")
        obj.callback_headers = []
        container = ARObject._find_child_element(element, "CALLBACK-HEADERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.callback_headers.append(child_value)

        return obj



class CodeBuilder:
    """Builder for Code."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Code = Code()

    def build(self) -> Code:
        """Build and return Code object.

        Returns:
            Code instance
        """
        # TODO: Add validation
        return self._obj
