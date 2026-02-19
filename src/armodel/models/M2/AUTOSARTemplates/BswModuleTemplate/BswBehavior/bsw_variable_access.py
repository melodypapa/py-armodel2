"""BswVariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 81)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswVariableAccess(Referrable):
    """AUTOSAR BswVariableAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_variable_ref: Optional[ARRef]
    contexts: list[BswDistinguishedPartition]
    def __init__(self) -> None:
        """Initialize BswVariableAccess."""
        super().__init__()
        self.accessed_variable_ref: Optional[ARRef] = None
        self.contexts: list[BswDistinguishedPartition] = []

    def serialize(self) -> ET.Element:
        """Serialize BswVariableAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswVariableAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_variable_ref
        if self.accessed_variable_ref is not None:
            serialized = ARObject._serialize_item(self.accessed_variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSED-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contexts (list to container "CONTEXTS")
        if self.contexts:
            wrapper = ET.Element("CONTEXTS")
            for item in self.contexts:
                serialized = ARObject._serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswVariableAccess":
        """Deserialize XML element to BswVariableAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswVariableAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswVariableAccess, cls).deserialize(element)

        # Parse accessed_variable_ref
        child = ARObject._find_child_element(element, "ACCESSED-VARIABLE-REF")
        if child is not None:
            accessed_variable_ref_value = ARRef.deserialize(child)
            obj.accessed_variable_ref = accessed_variable_ref_value

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        return obj



class BswVariableAccessBuilder:
    """Builder for BswVariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswVariableAccess = BswVariableAccess()

    def build(self) -> BswVariableAccess:
        """Build and return BswVariableAccess object.

        Returns:
            BswVariableAccess instance
        """
        # TODO: Add validation
        return self._obj
