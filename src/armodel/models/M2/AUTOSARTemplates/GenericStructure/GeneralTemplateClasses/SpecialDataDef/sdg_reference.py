"""SdgReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgReference(SdgAttribute):
    """AUTOSAR SdgReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dest_sdg_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SdgReference."""
        super().__init__()
        self.dest_sdg_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dest_sdg_ref
        if self.dest_sdg_ref is not None:
            serialized = ARObject._serialize_item(self.dest_sdg_ref, "SdgClass")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEST-SDG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgReference":
        """Deserialize XML element to SdgReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgReference, cls).deserialize(element)

        # Parse dest_sdg_ref
        child = ARObject._find_child_element(element, "DEST-SDG-REF")
        if child is not None:
            dest_sdg_ref_value = ARRef.deserialize(child)
            obj.dest_sdg_ref = dest_sdg_ref_value

        return obj



class SdgReferenceBuilder:
    """Builder for SdgReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgReference = SdgReference()

    def build(self) -> SdgReference:
        """Build and return SdgReference object.

        Returns:
            SdgReference instance
        """
        # TODO: Add validation
        return self._obj
