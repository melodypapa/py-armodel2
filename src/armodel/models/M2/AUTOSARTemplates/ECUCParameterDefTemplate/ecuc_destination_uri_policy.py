"""EcucDestinationUriPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    reference_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriPolicy."""
        super().__init__()
        self.containers: list[EcucContainerDef] = []
        self.destination_uri: Optional[Any] = None
        self.parameters: list[EcucParameterDef] = []
        self.reference_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = ARObject._serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize destination_uri
        if self.destination_uri is not None:
            serialized = ARObject._serialize_item(self.destination_uri, "Any")
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
                serialized = ARObject._serialize_item(item, "EcucParameterDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_refs (list to container "REFERENCES")
        if self.reference_refs:
            wrapper = ET.Element("REFERENCES")
            for item in self.reference_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse containers (list from container "CONTAINERS")
        obj.containers = []
        container = ARObject._find_child_element(element, "CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.containers.append(child_value)

        # Parse destination_uri
        child = ARObject._find_child_element(element, "DESTINATION-URI")
        if child is not None:
            destination_uri_value = child.text
            obj.destination_uri = destination_uri_value

        # Parse parameters (list from container "PARAMETERS")
        obj.parameters = []
        container = ARObject._find_child_element(element, "PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameters.append(child_value)

        # Parse reference_refs (list from container "REFERENCES")
        obj.reference_refs = []
        container = ARObject._find_child_element(element, "REFERENCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
