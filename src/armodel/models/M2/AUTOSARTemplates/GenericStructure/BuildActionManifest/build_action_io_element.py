"""BuildActionIoElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionIoElement(ARObject):
    """AUTOSAR BuildActionIoElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: NameToken
    ecuc_definition: Optional[EcucDefinitionElement]
    role: Optional[Identifier]
    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize BuildActionIoElement."""
        super().__init__()
        self.category: NameToken = None
        self.ecuc_definition: Optional[EcucDefinitionElement] = None
        self.role: Optional[Identifier] = None
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize BuildActionIoElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_definition
        if self.ecuc_definition is not None:
            serialized = ARObject._serialize_item(self.ecuc_definition, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-DEFINITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = ARObject._serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = ARObject._serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionIoElement":
        """Deserialize XML element to BuildActionIoElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionIoElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse ecuc_definition
        child = ARObject._find_child_element(element, "ECUC-DEFINITION")
        if child is not None:
            ecuc_definition_value = ARObject._deserialize_by_tag(child, "EcucDefinitionElement")
            obj.ecuc_definition = ecuc_definition_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse sdgs (list from container "SDGS")
        obj.sdgs = []
        container = ARObject._find_child_element(element, "SDGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdgs.append(child_value)

        return obj



class BuildActionIoElementBuilder:
    """Builder for BuildActionIoElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionIoElement = BuildActionIoElement()

    def build(self) -> BuildActionIoElement:
        """Build and return BuildActionIoElement object.

        Returns:
            BuildActionIoElement instance
        """
        # TODO: Add validation
        return self._obj
