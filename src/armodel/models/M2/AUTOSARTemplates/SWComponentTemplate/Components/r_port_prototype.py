"""RPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 460)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    may_be: Optional[Boolean]
    required: Optional[PortInterface]
    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be: Optional[Boolean] = None
        self.required: Optional[PortInterface] = None

    def serialize(self) -> ET.Element:
        """Serialize RPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize may_be
        if self.may_be is not None:
            serialized = ARObject._serialize_item(self.may_be, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAY-BE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required
        if self.required is not None:
            serialized = ARObject._serialize_item(self.required, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortPrototype":
        """Deserialize XML element to RPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RPortPrototype, cls).deserialize(element)

        # Parse may_be
        child = ARObject._find_child_element(element, "MAY-BE")
        if child is not None:
            may_be_value = child.text
            obj.may_be = may_be_value

        # Parse required
        child = ARObject._find_child_element(element, "REQUIRED")
        if child is not None:
            required_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.required = required_value

        return obj



class RPortPrototypeBuilder:
    """Builder for RPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortPrototype = RPortPrototype()

    def build(self) -> RPortPrototype:
        """Build and return RPortPrototype object.

        Returns:
            RPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
