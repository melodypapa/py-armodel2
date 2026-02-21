"""PPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2041)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PPortPrototype(AbstractProvidedPortPrototype):
    """AUTOSAR PPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided_interface_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PPortPrototype."""
        super().__init__()
        self.provided_interface_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_interface_ref
        if self.provided_interface_ref is not None:
            serialized = ARObject._serialize_item(self.provided_interface_ref, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-INTERFACE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortPrototype":
        """Deserialize XML element to PPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PPortPrototype, cls).deserialize(element)

        # Parse provided_interface_ref
        child = ARObject._find_child_element(element, "PROVIDED-INTERFACE-TREF")
        if child is not None:
            provided_interface_ref_value = ARRef.deserialize(child)
            obj.provided_interface_ref = provided_interface_ref_value

        return obj



class PPortPrototypeBuilder:
    """Builder for PPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortPrototype = PPortPrototype()

    def build(self) -> PPortPrototype:
        """Build and return PPortPrototype object.

        Returns:
            PPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
