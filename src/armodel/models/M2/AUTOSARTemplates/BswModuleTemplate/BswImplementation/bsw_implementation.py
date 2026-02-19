"""BswImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 120)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 290)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 207)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    behavior: Optional[BswInternalBehavior]
    preconfigureds: list[Any]
    recommendeds: list[Any]
    vendor_api_infix: Optional[Identifier]
    vendor_specifics: list[EcucModuleDef]
    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior: Optional[BswInternalBehavior] = None
        self.preconfigureds: list[Any] = []
        self.recommendeds: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specifics: list[EcucModuleDef] = []
    def serialize(self) -> ET.Element:
        """Serialize BswImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_release
        if self.ar_release is not None:
            serialized = ARObject._serialize_item(self.ar_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize behavior
        if self.behavior is not None:
            serialized = ARObject._serialize_item(self.behavior, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize preconfigureds (list to container "PRECONFIGUREDS")
        if self.preconfigureds:
            wrapper = ET.Element("PRECONFIGUREDS")
            for item in self.preconfigureds:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize recommendeds (list to container "RECOMMENDEDS")
        if self.recommendeds:
            wrapper = ET.Element("RECOMMENDEDS")
            for item in self.recommendeds:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize vendor_api_infix
        if self.vendor_api_infix is not None:
            serialized = ARObject._serialize_item(self.vendor_api_infix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR-API-INFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor_specifics (list to container "VENDOR-SPECIFICS")
        if self.vendor_specifics:
            wrapper = ET.Element("VENDOR-SPECIFICS")
            for item in self.vendor_specifics:
                serialized = ARObject._serialize_item(item, "EcucModuleDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswImplementation":
        """Deserialize XML element to BswImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswImplementation, cls).deserialize(element)

        # Parse ar_release
        child = ARObject._find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse behavior
        child = ARObject._find_child_element(element, "BEHAVIOR")
        if child is not None:
            behavior_value = ARObject._deserialize_by_tag(child, "BswInternalBehavior")
            obj.behavior = behavior_value

        # Parse preconfigureds (list from container "PRECONFIGUREDS")
        obj.preconfigureds = []
        container = ARObject._find_child_element(element, "PRECONFIGUREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.preconfigureds.append(child_value)

        # Parse recommendeds (list from container "RECOMMENDEDS")
        obj.recommendeds = []
        container = ARObject._find_child_element(element, "RECOMMENDEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.recommendeds.append(child_value)

        # Parse vendor_api_infix
        child = ARObject._find_child_element(element, "VENDOR-API-INFIX")
        if child is not None:
            vendor_api_infix_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.vendor_api_infix = vendor_api_infix_value

        # Parse vendor_specifics (list from container "VENDOR-SPECIFICS")
        obj.vendor_specifics = []
        container = ARObject._find_child_element(element, "VENDOR-SPECIFICS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vendor_specifics.append(child_value)

        return obj



class BswImplementationBuilder:
    """Builder for BswImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswImplementation = BswImplementation()

    def build(self) -> BswImplementation:
        """Build and return BswImplementation object.

        Returns:
            BswImplementation instance
        """
        # TODO: Add validation
        return self._obj
