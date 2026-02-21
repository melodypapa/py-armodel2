"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lc_object_ref: ARRef
    lc_state_ref: Optional[ARRef]
    period_begin: Optional[LifeCyclePeriod]
    period_end: Optional[LifeCyclePeriod]
    remark: Optional[DocumentationBlock]
    use_instead_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object_ref: ARRef = None
        self.lc_state_ref: Optional[ARRef] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_instead_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lc_object_ref
        if self.lc_object_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_object_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-OBJECT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lc_state_ref
        if self.lc_state_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lc_state_ref, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LC-STATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_begin
        if self.period_begin is not None:
            serialized = SerializationHelper.serialize_item(self.period_begin, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-BEGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period_end
        if self.period_end is not None:
            serialized = SerializationHelper.serialize_item(self.period_end, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remark
        if self.remark is not None:
            serialized = SerializationHelper.serialize_item(self.remark, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMARK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_instead_refs (list to container "USE-INSTEAD-REFS")
        if self.use_instead_refs:
            wrapper = ET.Element("USE-INSTEAD-REFS")
            for item in self.use_instead_refs:
                serialized = SerializationHelper.serialize_item(item, "Referrable")
                if serialized is not None:
                    child_elem = ET.Element("USE-INSTEAD-REF")
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
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfo":
        """Deserialize XML element to LifeCycleInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfo, cls).deserialize(element)

        # Parse lc_object_ref
        child = SerializationHelper.find_child_element(element, "LC-OBJECT-REF")
        if child is not None:
            lc_object_ref_value = ARRef.deserialize(child)
            obj.lc_object_ref = lc_object_ref_value

        # Parse lc_state_ref
        child = SerializationHelper.find_child_element(element, "LC-STATE-REF")
        if child is not None:
            lc_state_ref_value = ARRef.deserialize(child)
            obj.lc_state_ref = lc_state_ref_value

        # Parse period_begin
        child = SerializationHelper.find_child_element(element, "PERIOD-BEGIN")
        if child is not None:
            period_begin_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.period_begin = period_begin_value

        # Parse period_end
        child = SerializationHelper.find_child_element(element, "PERIOD-END")
        if child is not None:
            period_end_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.period_end = period_end_value

        # Parse remark
        child = SerializationHelper.find_child_element(element, "REMARK")
        if child is not None:
            remark_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.remark = remark_value

        # Parse use_instead_refs (list from container "USE-INSTEAD-REFS")
        obj.use_instead_refs = []
        container = SerializationHelper.find_child_element(element, "USE-INSTEAD-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.use_instead_refs.append(child_value)

        return obj



class LifeCycleInfoBuilder:
    """Builder for LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfo = LifeCycleInfo()

    def build(self) -> LifeCycleInfo:
        """Build and return LifeCycleInfo object.

        Returns:
            LifeCycleInfo instance
        """
        # TODO: Add validation
        return self._obj
