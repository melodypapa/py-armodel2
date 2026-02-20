"""RptHook AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 848)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class RptHook(ARObject):
    """AUTOSAR RptHook."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    code_label: Optional[CIdentifier]
    mcd_identifier: Optional[NameToken]
    rpt_ar_hook: Optional[AtpFeature]
    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize RptHook."""
        super().__init__()
        self.code_label: Optional[CIdentifier] = None
        self.mcd_identifier: Optional[NameToken] = None
        self.rpt_ar_hook: Optional[AtpFeature] = None
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize RptHook to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize code_label
        if self.code_label is not None:
            serialized = ARObject._serialize_item(self.code_label, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CODE-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mcd_identifier
        if self.mcd_identifier is not None:
            serialized = ARObject._serialize_item(self.mcd_identifier, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MCD-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_ar_hook
        if self.rpt_ar_hook is not None:
            serialized = ARObject._serialize_item(self.rpt_ar_hook, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-AR-HOOK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = ARObject._serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptHook":
        """Deserialize XML element to RptHook object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptHook object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse code_label
        child = ARObject._find_child_element(element, "CODE-LABEL")
        if child is not None:
            code_label_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.code_label = code_label_value

        # Parse mcd_identifier
        child = ARObject._find_child_element(element, "MCD-IDENTIFIER")
        if child is not None:
            mcd_identifier_value = child.text
            obj.mcd_identifier = mcd_identifier_value

        # Parse rpt_ar_hook
        child = ARObject._find_child_element(element, "RPT-AR-HOOK")
        if child is not None:
            rpt_ar_hook_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.rpt_ar_hook = rpt_ar_hook_value

        # Parse sdgs (list from container "SDGS")
        obj.sdgs = []
        container = ARObject._find_child_element(element, "SDGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdgs.append(child_value)

        return obj



class RptHookBuilder:
    """Builder for RptHook."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptHook = RptHook()

    def build(self) -> RptHook:
        """Build and return RptHook object.

        Returns:
            RptHook instance
        """
        # TODO: Add validation
        return self._obj
