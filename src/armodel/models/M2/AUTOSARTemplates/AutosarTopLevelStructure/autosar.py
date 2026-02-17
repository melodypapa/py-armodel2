"""AUTOSAR AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 298)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 287)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 59)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 968)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1993)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 203)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 42)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 71)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 56)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.serialization.name_converter import NameConverter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.file_info_comment import (
    FileInfoComment,
)


class AUTOSAR(ARObject):
    """AUTOSAR AUTOSAR root element.

    This is the root element of any ARXML document. As the root element,
    it handles namespace attributes that should appear only once in the document.
    """

    admin_data: Optional[AdminData]
    ar_packages: list[ARPackage]
    file_info: Optional[FileInfoComment]
    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize AUTOSAR."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.ar_packages: list[ARPackage] = []
        self.file_info: Optional[FileInfoComment] = None
        self.introduction: Optional[DocumentationBlock] = None

    def serialize(self) -> ET.Element:
        """Serialize AUTOSAR root element to XML with namespace attributes.

        As the root element of ARXML documents, AUTOSAR handles namespace
        attributes. Child elements inherit from this root and do not need
        their own namespace declarations.

        Returns:
            xml.etree.ElementTree.Element representing the AUTOSAR root element
        """
        # Get XML tag name using parent method
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Add AUTOSAR namespace attributes (root element only)
        elem.set("xmlns", "http://autosar.org/schema/r4.0")
        elem.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        elem.set("xsi:schemaLocation", "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd")

        # Serialize all instance attributes
        for name, value in vars(self).items():
            # Skip private attributes
            if name.startswith('_'):
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(name)

            # Skip None values
            if value is None:
                continue

            # Check if this should be an XML attribute (via decorator)
            if self._is_xml_attribute(name):
                elem.set(xml_tag, str(value))
            elif hasattr(value, 'serialize'):
                # Recursively serialize child objects (no namespace parameter)
                child = value.serialize()
                elem.append(child)
            elif isinstance(value, list):
                # Serialize list items - create wrapper element
                wrapper = ET.Element(xml_tag)
                for item in value:
                    if hasattr(item, 'serialize'):
                        wrapper.append(item.serialize())
                    else:
                        child = ET.Element(xml_tag)
                        child.text = str(item)
                        wrapper.append(child)
                elem.append(wrapper)
            else:
                # Primitive value - create element with text content
                child = ET.Element(xml_tag)
                child.text = str(value)
                elem.append(child)

        return elem


class AUTOSARBuilder:
    """Builder for AUTOSAR."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AUTOSAR = AUTOSAR()

    def build(self) -> AUTOSAR:
        """Build and return AUTOSAR object.

        Returns:
            AUTOSAR instance
        """
        # TODO: Add validation
        return self._obj