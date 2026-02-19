"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    short_label: Identifier
    is_default: Boolean
    is_global: Boolean
    base_is_this_package: Boolean
    package_ref: Optional[ARRef]
    global_element_refs: list[ReferrableSubtypesEnum]
    global_in_package_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.short_label: Identifier = None
        self.is_default: Boolean = None
        self.is_global: Boolean = None
        self.base_is_this_package: Boolean = None
        self.package_ref: Optional[ARRef] = None
        self.global_element_refs: list[ReferrableSubtypesEnum] = []
        self.global_in_package_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize ReferenceBase to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_default
        if self.is_default is not None:
            serialized = ARObject._serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_global
        if self.is_global is not None:
            serialized = ARObject._serialize_item(self.is_global, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-GLOBAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_is_this_package
        if self.base_is_this_package is not None:
            serialized = ARObject._serialize_item(self.base_is_this_package, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-IS-THIS-PACKAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize package_ref
        if self.package_ref is not None:
            serialized = ARObject._serialize_item(self.package_ref, "ARPackage")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_element_refs (list to container "GLOBAL-ELEMENTS")
        if self.global_element_refs:
            wrapper = ET.Element("GLOBAL-ELEMENTS")
            for item in self.global_element_refs:
                serialized = ARObject._serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_in_package_refs (list to container "GLOBAL-IN-PACKAGES")
        if self.global_in_package_refs:
            wrapper = ET.Element("GLOBAL-IN-PACKAGES")
            for item in self.global_in_package_refs:
                serialized = ARObject._serialize_item(item, "ARPackage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Deserialize XML element to ReferenceBase object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceBase object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse is_global
        child = ARObject._find_child_element(element, "IS-GLOBAL")
        if child is not None:
            is_global_value = child.text
            obj.is_global = is_global_value

        # Parse base_is_this_package
        child = ARObject._find_child_element(element, "BASE-IS-THIS-PACKAGE")
        if child is not None:
            base_is_this_package_value = child.text
            obj.base_is_this_package = base_is_this_package_value

        # Parse package_ref
        child = ARObject._find_child_element(element, "PACKAGE-REF")
        if child is not None:
            package_ref_value = ARRef.deserialize(child)
            obj.package_ref = package_ref_value

        # Parse global_element_refs (list from container "GLOBAL-ELEMENTS")
        obj.global_element_refs = []
        container = ARObject._find_child_element(element, "GLOBAL-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_element_refs.append(child_value)

        # Parse global_in_package_refs (list from container "GLOBAL-IN-PACKAGES")
        obj.global_in_package_refs = []
        container = ARObject._find_child_element(element, "GLOBAL-IN-PACKAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_in_package_refs.append(child_value)

        return obj



class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
