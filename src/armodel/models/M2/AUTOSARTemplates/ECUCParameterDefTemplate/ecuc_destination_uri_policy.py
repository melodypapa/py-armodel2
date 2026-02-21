"""EcucDestinationUriPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucDestinationUriPolicy(ARObject):
    """AUTOSAR EcucDestinationUriPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    containers: list[EcucContainerDef]
    destination_uri: Optional[Any]
    parameters: list[EcucParameterDef]
    reference_refs: list[Any]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize destination_uri
        if self.destination_uri is not None:
            serialized = SerializationHelper.serialize_item(self.destination_uri, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-URI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameters (list to container "PARAMETERS")
        if self.parameters:
            wrapper = ET.Element("PARAMETERS")
            for item in self.parameters:
                serialized = SerializationHelper.serialize_item(item, "EcucParameterDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_refs (list to container "REFERENCE-REFS")
        if self.reference_refs:
            wrapper = ET.Element("REFERENCE-REFS")
            for item in self.reference_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriPolicy":
        """Deserialize XML element to EcucDestinationUriPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriPolicy, cls).deserialize(element)

        # Parse containers (list from container "CONTAINERS")
        obj.containers = []
        container = SerializationHelper.find_child_element(element, "CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.containers.append(child_value)

        # Parse destination_uri
        child = SerializationHelper.find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = child.text
            obj.destination_uri = destination_uri_value

        # Parse parameters (list from container "PARAMETERS")
        obj.parameters = []
        container = SerializationHelper.find_child_element(element, "PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameters.append(child_value)

        # Parse reference_refs (list from container "REFERENCE-REFS")
        obj.reference_refs = []
        container = SerializationHelper.find_child_element(element, "REFERENCE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reference_refs.append(child_value)

        return obj



class EcucDestinationUriPolicyBuilder:
    """Builder for EcucDestinationUriPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriPolicy = EcucDestinationUriPolicy()

    def build(self) -> EcucDestinationUriPolicy:
        """Build and return EcucDestinationUriPolicy object.

        Returns:
            EcucDestinationUriPolicy instance
        """
        # TODO: Add validation
        return self._obj
