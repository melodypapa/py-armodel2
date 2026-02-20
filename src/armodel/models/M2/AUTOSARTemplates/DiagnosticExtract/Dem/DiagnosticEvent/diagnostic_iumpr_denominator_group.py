"""DiagnosticIumprDenominatorGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprDenominatorGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprDenominatorGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iumpr_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprDenominatorGroup."""
        super().__init__()
        self.iumpr_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumprDenominatorGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumprDenominatorGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize iumpr_refs (list to container "IUMPR-REFS")
        if self.iumpr_refs:
            wrapper = ET.Element("IUMPR-REFS")
            for item in self.iumpr_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticIumpr")
                if serialized is not None:
                    child_elem = ET.Element("IUMPR-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprDenominatorGroup":
        """Deserialize XML element to DiagnosticIumprDenominatorGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprDenominatorGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprDenominatorGroup, cls).deserialize(element)

        # Parse iumpr_refs (list from container "IUMPR-REFS")
        obj.iumpr_refs = []
        container = ARObject._find_child_element(element, "IUMPR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.iumpr_refs.append(child_value)

        return obj



class DiagnosticIumprDenominatorGroupBuilder:
    """Builder for DiagnosticIumprDenominatorGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprDenominatorGroup = DiagnosticIumprDenominatorGroup()

    def build(self) -> DiagnosticIumprDenominatorGroup:
        """Build and return DiagnosticIumprDenominatorGroup object.

        Returns:
            DiagnosticIumprDenominatorGroup instance
        """
        # TODO: Add validation
        return self._obj
