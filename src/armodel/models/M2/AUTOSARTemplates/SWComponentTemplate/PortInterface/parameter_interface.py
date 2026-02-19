"""ParameterInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterInterface(DataInterface):
    """AUTOSAR ParameterInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameter_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ParameterInterface."""
        super().__init__()
        self.parameter_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize ParameterInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize parameter_refs (list to container "PARAMETERS")
        if self.parameter_refs:
            wrapper = ET.Element("PARAMETERS")
            for item in self.parameter_refs:
                serialized = ARObject._serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterInterface":
        """Deserialize XML element to ParameterInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterInterface, cls).deserialize(element)

        # Parse parameter_refs (list from container "PARAMETERS")
        obj.parameter_refs = []
        container = ARObject._find_child_element(element, "PARAMETERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_refs.append(child_value)

        return obj



class ParameterInterfaceBuilder:
    """Builder for ParameterInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterInterface = ParameterInterface()

    def build(self) -> ParameterInterface:
        """Build and return ParameterInterface object.

        Returns:
            ParameterInterface instance
        """
        # TODO: Add validation
        return self._obj
