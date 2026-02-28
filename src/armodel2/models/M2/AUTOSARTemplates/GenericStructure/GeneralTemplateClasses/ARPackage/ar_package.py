"""ARPackage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 297)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 286)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 58)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 967)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1992)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 203)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 53)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 55)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.reference_base import (
        ReferenceBase,
    )



class ARPackage(CollectableElement):
    """AUTOSAR ARPackage."""

    _XML_TAG = "AR-PACKAGE"

    _DESERIALIZE_DISPATCH = {
        "REFERENCE-BASES": lambda obj, elem: setattr(
            obj, "_reference_bases",
            [SerializationHelper.deserialize_by_tag(child, None) for child in elem if child.tag not in ("{http://www.w3.org/2001/XMLSchema-instance}", "{http://www.w3.org/2001/XMLSchema}")]
        ),
        "ELEMENTS": lambda obj, elem: setattr(
            obj, "_elements",
            [SerializationHelper.deserialize_by_tag(child, None) for child in elem if child.tag not in ("{http://www.w3.org/2001/XMLSchema-instance}", "{http://www.w3.org/2001/XMLSchema}")]
        ),
        "AR-PACKAGES": lambda obj, elem: setattr(
            obj, "_ar_packages",
            [SerializationHelper.deserialize_by_tag(child, None) for child in elem if child.tag not in ("{http://www.w3.org/2001/XMLSchema-instance}", "{http://www.w3.org/2001/XMLSchema}")]
        ),
    }

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    reference_bases: list[ReferenceBase]
    elements: list[PackageableElement]
    ar_packages: list[ARPackage]
    def __init__(self) -> None:
        """Initialize ARPackage."""
        super().__init__()
        self._reference_bases: list[ReferenceBase] = []
        self._elements: list[PackageableElement] = []
        self._ar_packages: list[ARPackage] = []
    def serialize(self) -> ET.Element:
        """Serialize ARPackage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ARPackage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize reference_bases (list to container "REFERENCE-BASES")
        if self._reference_bases:
            wrapper = ET.Element("REFERENCE-BASES")
            for item in self._reference_bases:
                serialized = SerializationHelper.serialize_item(item, "ReferenceBase")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize elements (list to container "ELEMENTS")
        if self._elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self._elements:
                serialized = SerializationHelper.serialize_item(item, "PackageableElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ar_packages (list to container "AR-PACKAGES")
        if self._ar_packages:
            wrapper = ET.Element("AR-PACKAGES")
            for item in self._ar_packages:
                serialized = SerializationHelper.serialize_item(item, "ARPackage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPackage":
        """Deserialize XML element to ARPackage object.

        Uses static dispatch table for O(1) tag-to-handler lookup.
        Calls super().deserialize() first to handle inherited attributes
        from the chain: ARPackage -> CollectableElement -> Identifiable ->
        MultilanguageReferrable -> Referrable -> ARObject.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPackage object
        """
        # First, deserialize inherited attributes from parent chain
        # The parent chain will create and return the object
        obj = super(ARPackage, cls).deserialize(element)

        # Then process ARPackage-specific elements with dispatch table
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)

        return obj


class ARPackageBuilder:
    """Builder for ARPackage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARPackage = ARPackage()

    def build(self) -> ARPackage:
        """Build and return ARPackage object.

        Returns:
            ARPackage instance
        """
        # TODO: Add validation
        return self._obj


# Add property getters and setters for ARPackage
def _get_reference_bases(self) -> list[ReferenceBase]:
    return self._reference_bases

def _set_reference_bases(self, value: list[ReferenceBase]) -> None:
    self._reference_bases = value

def _get_elements(self) -> list[PackageableElement]:
    return self._elements

def _set_elements(self, value: list[PackageableElement]) -> None:
    self._elements = value

def _get_ar_packages(self) -> list[ARPackage]:
    return self._ar_packages

def _set_ar_packages(self, value: list[ARPackage]) -> None:
    self._ar_packages = value

ARPackage.reference_bases = property(_get_reference_bases, _set_reference_bases)
ARPackage.elements = property(_get_elements, _set_elements)
ARPackage.ar_packages = property(_get_ar_packages, _set_ar_packages)
