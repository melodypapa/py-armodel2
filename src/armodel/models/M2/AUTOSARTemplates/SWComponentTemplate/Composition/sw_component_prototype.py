"""SwComponentPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 77)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 896)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 245)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 466)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = ARObject._serialize_item(self.type_ref, "SwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototype":
        """Deserialize XML element to SwComponentPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentPrototype, cls).deserialize(element)

        # Parse type_ref
        child = ARObject._find_child_element(element, "TYPE-TREF")
        if child is not None:
            type_ref_value = ARRef.deserialize(child)
            obj.type_ref = type_ref_value

        return obj



class SwComponentPrototypeBuilder:
    """Builder for SwComponentPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototype = SwComponentPrototype()

    def build(self) -> SwComponentPrototype:
        """Build and return SwComponentPrototype object.

        Returns:
            SwComponentPrototype instance
        """
        # TODO: Add validation
        return self._obj
