"""EcucContainerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 119)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2021)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition: Optional[EcucContainerDef]
    parameter_values: list[EcucParameterValue]
    reference_value_refs: list[Any]
    sub_containers: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition: Optional[EcucContainerDef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_value_refs: list[Any] = []
        self.sub_containers: list[EcucContainerValue] = []
    def serialize(self) -> ET.Element:
        """Serialize EcucContainerValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucContainerValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize definition
        if self.definition is not None:
            serialized = ARObject._serialize_item(self.definition, "EcucContainerDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter_values (list to container "PARAMETER-VALUES")
        if self.parameter_values:
            wrapper = ET.Element("PARAMETER-VALUES")
            for item in self.parameter_values:
                serialized = ARObject._serialize_item(item, "EcucParameterValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_value_refs (list to container "REFERENCE-VALUES")
        if self.reference_value_refs:
            wrapper = ET.Element("REFERENCE-VALUES")
            for item in self.reference_value_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_containers (list to container "SUB-CONTAINERS")
        if self.sub_containers:
            wrapper = ET.Element("SUB-CONTAINERS")
            for item in self.sub_containers:
                serialized = ARObject._serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerValue":
        """Deserialize XML element to EcucContainerValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucContainerValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucContainerValue, cls).deserialize(element)

        # Parse definition
        child = ARObject._find_child_element(element, "DEFINITION")
        if child is not None:
            definition_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.definition = definition_value

        # Parse parameter_values (list from container "PARAMETER-VALUES")
        obj.parameter_values = []
        container = ARObject._find_child_element(element, "PARAMETER-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_values.append(child_value)

        # Parse reference_value_refs (list from container "REFERENCE-VALUES")
        obj.reference_value_refs = []
        container = ARObject._find_child_element(element, "REFERENCE-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reference_value_refs.append(child_value)

        # Parse sub_containers (list from container "SUB-CONTAINERS")
        obj.sub_containers = []
        container = ARObject._find_child_element(element, "SUB-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_containers.append(child_value)

        return obj



class EcucContainerValueBuilder:
    """Builder for EcucContainerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerValue = EcucContainerValue()

    def build(self) -> EcucContainerValue:
        """Build and return EcucContainerValue object.

        Returns:
            EcucContainerValue instance
        """
        # TODO: Add validation
        return self._obj
