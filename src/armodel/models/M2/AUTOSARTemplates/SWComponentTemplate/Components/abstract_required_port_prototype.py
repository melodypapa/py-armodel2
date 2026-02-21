"""AbstractRequiredPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from abc import ABC, abstractmethod


class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractRequiredPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    required_coms: list[RPortComSpec]
    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self.required_coms: list[RPortComSpec] = []

    def serialize(self) -> ET.Element:
        """Serialize AbstractRequiredPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractRequiredPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize required_coms (list to container "REQUIRED-COMS")
        if self.required_coms:
            wrapper = ET.Element("REQUIRED-COMS")
            for item in self.required_coms:
                serialized = ARObject._serialize_item(item, "RPortComSpec")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractRequiredPortPrototype":
        """Deserialize XML element to AbstractRequiredPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractRequiredPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractRequiredPortPrototype, cls).deserialize(element)

        # Parse required_coms (list from container "REQUIRED-COMS")
        obj.required_coms = []
        container = ARObject._find_child_element(element, "REQUIRED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_coms.append(child_value)

        return obj



class AbstractRequiredPortPrototypeBuilder:
    """Builder for AbstractRequiredPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()

    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return AbstractRequiredPortPrototype object.

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
