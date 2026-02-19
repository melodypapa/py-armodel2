"""ApplicationInterface AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AbstractPlatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface.field import (
    Field,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ApplicationInterface(PortInterface):
    """AUTOSAR ApplicationInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[Field]
    commands: list[ClientServerOperation]
    indication_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ApplicationInterface."""
        super().__init__()
        self.attributes: list[Field] = []
        self.commands: list[ClientServerOperation] = []
        self.indication_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize ApplicationInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attributes (list to container "ATTRIBUTES")
        if self.attributes:
            wrapper = ET.Element("ATTRIBUTES")
            for item in self.attributes:
                serialized = ARObject._serialize_item(item, "Field")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize commands (list to container "COMMANDS")
        if self.commands:
            wrapper = ET.Element("COMMANDS")
            for item in self.commands:
                serialized = ARObject._serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize indication_refs (list to container "INDICATIONS")
        if self.indication_refs:
            wrapper = ET.Element("INDICATIONS")
            for item in self.indication_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationInterface":
        """Deserialize XML element to ApplicationInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationInterface, cls).deserialize(element)

        # Parse attributes (list from container "ATTRIBUTES")
        obj.attributes = []
        container = ARObject._find_child_element(element, "ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attributes.append(child_value)

        # Parse commands (list from container "COMMANDS")
        obj.commands = []
        container = ARObject._find_child_element(element, "COMMANDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.commands.append(child_value)

        # Parse indication_refs (list from container "INDICATIONS")
        obj.indication_refs = []
        container = ARObject._find_child_element(element, "INDICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.indication_refs.append(child_value)

        return obj



class ApplicationInterfaceBuilder:
    """Builder for ApplicationInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationInterface = ApplicationInterface()

    def build(self) -> ApplicationInterface:
        """Build and return ApplicationInterface object.

        Returns:
            ApplicationInterface instance
        """
        # TODO: Add validation
        return self._obj
