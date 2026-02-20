"""EcucParamConfContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucParamConfContainerDef(EcucContainerDef):
    """AUTOSAR EcucParamConfContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameters: list[EcucParameterDef]
    reference_refs: list[Any]
    sub_containers: list[EcucContainerDef]
    def __init__(self) -> None:
        """Initialize EcucParamConfContainerDef."""
        super().__init__()
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[Any] = []
        self.sub_containers: list[EcucContainerDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucParamConfContainerDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParamConfContainerDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize parameters (list to container "PARAMETERS")
        if self.parameters:
            wrapper = ET.Element("PARAMETERS")
            for item in self.parameters:
                serialized = ARObject._serialize_item(item, "EcucParameterDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_refs (list to container "REFERENCE-REFS")
        if self.reference_refs:
            wrapper = ET.Element("REFERENCE-REFS")
            for item in self.reference_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("REFERENCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_containers (list to container "SUB-CONTAINERS")
        if self.sub_containers:
            wrapper = ET.Element("SUB-CONTAINERS")
            for item in self.sub_containers:
                serialized = ARObject._serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParamConfContainerDef":
        """Deserialize XML element to EcucParamConfContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParamConfContainerDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParamConfContainerDef, cls).deserialize(element)

        # Parse parameters (list from container "PARAMETERS")
        obj.parameters = []
        container = ARObject._find_child_element(element, "PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameters.append(child_value)

        # Parse reference_refs (list from container "REFERENCE-REFS")
        obj.reference_refs = []
        container = ARObject._find_child_element(element, "REFERENCE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reference_refs.append(child_value)

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



class EcucParamConfContainerDefBuilder:
    """Builder for EcucParamConfContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParamConfContainerDef = EcucParamConfContainerDef()

    def build(self) -> EcucParamConfContainerDef:
        """Build and return EcucParamConfContainerDef object.

        Returns:
            EcucParamConfContainerDef instance
        """
        # TODO: Add validation
        return self._obj
