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
        self.reference_bases: list[ReferenceBase] = []
        self.elements: list[PackageableElement] = []
        self.ar_packages: list[ARPackage] = []
    def serialize(self) -> ET.Element:
        """Serialize ARPackage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ARPackage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize reference_bases (list to container "REFERENCE-BASES")
        if self.reference_bases:
            wrapper = ET.Element("REFERENCE-BASES")
            for item in self.reference_bases:
                serialized = SerializationHelper.serialize_item(item, "ReferenceBase")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = SerializationHelper.serialize_item(item, "PackageableElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ar_packages (list to container "AR-PACKAGES")
        if self.ar_packages:
            wrapper = ET.Element("AR-PACKAGES")
            for item in self.ar_packages:
                serialized = SerializationHelper.serialize_item(item, "ARPackage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPackage":
        """Deserialize XML element to ARPackage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPackage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ARPackage, cls).deserialize(element)

        # Parse reference_bases (list from container "REFERENCE-BASES")
        obj.reference_bases = []
        container = SerializationHelper.find_child_element(element, "REFERENCE-BASES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reference_bases.append(child_value)

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = SerializationHelper.find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        # Parse ar_packages (list from container "AR-PACKAGES")
        obj.ar_packages = []
        container = SerializationHelper.find_child_element(element, "AR-PACKAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_packages.append(child_value)

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
