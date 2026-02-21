"""PRPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PRPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR PRPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided: Optional[PortInterface]
    def __init__(self) -> None:
        """Initialize PRPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None

    def serialize(self) -> ET.Element:
        """Serialize PRPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PRPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided
        if self.provided is not None:
            serialized = SerializationHelper.serialize_item(self.provided, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PRPortPrototype":
        """Deserialize XML element to PRPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PRPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PRPortPrototype, cls).deserialize(element)

        # Parse provided
        child = SerializationHelper.find_child_element(element, "PROVIDED")
        if child is not None:
            provided_value = SerializationHelper.deserialize_by_tag(child, "PortInterface")
            obj.provided = provided_value

        return obj



class PRPortPrototypeBuilder:
    """Builder for PRPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PRPortPrototype = PRPortPrototype()

    def build(self) -> PRPortPrototype:
        """Build and return PRPortPrototype object.

        Returns:
            PRPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
